Asset Cloud
===========

Asset Cloud is a Cloud-based, highly configurable light-weight DAM system.

Asset Cloud is the base application of Asset Share, and there are some references to Asset Share throughout the application, mostly in static files and templates.

Please see the [AssetCloud Wiki](http://wiki.bright-interactive.com/display/knowhow/Asset+Cloud) for more of an overview.

See the [Project Backlog](https://spreadsheets.google.com/a/bright-interactive.co.uk/spreadsheet/ccc?key=0AgTdJwbo2dsWdEY0MnRWVWlCQ01pVGtJNjcxYXNJRHc&hl=en_US) for features, timescales & planning.

Prerequisites
-------------

* python 2.7 (wide build, i.e. configured with --enable-unicode=ucs4)
* virtualenv
* libjpeg or jpeg

If you don't want to use a wide build of Python on a *developer* machine then you can add `WIDE_CHAR_TESTS = False` to `project/settings/local_common.py`.

If you are using MacPorts use:

    sudo port install python27 +ucs4
    sudo port install py27-virtualenv
    sudo port install jpeg

If you are running Mac OSX, you will need the following items to run the Selenium tests:

    Google Chrome - Installation instructions and download at https://www.google.com/intl/en/chrome/browser/   
    chromedriver - Installation instructions and download at http://code.google.com/p/chromedriver/downloads/list


Installation
------------

To clone the repo:

    git clone git@github.com:brightinteractive/assetcloud.git

To setup:

    . ./activate

To run the project:

    . ./activate
    ./manage syncdb --noinput --migrate
    ./manage runserver
    # Login with `admin@bright-interactive.co.uk`/`password`

To run the tests:

    ./manage test apps assetcloud_example

If you are running the tests on Mac OSX, you will need to configure Selenium to use chromedriver by including the following lines in your local settings file (project/settings/local_common.py):

    import os
    WEBDRIVERPLUS_BROWSER ='chrome'
    # Put /usr/local/bin on the PATH so that /usr/local/bin/chromedriver can be found
    os.environ['PATH'] = '/usr/local/bin:' + os.environ['PATH']

Because Assetcloud is a reusable application, it is very important to always use named URLs.
To make sure that this is being done, there is a second testing configuration which runs all the tests on an alternative url layout.
You can run tests for this layout using ./manage test apps assetcloud_example --settings=settings.testing_alternative_urls.
You don't have to run the full test suite for both configurations, but it's recommended that you do run it for your new tests.

Upgrading to version 0.15.x and above
-------------------------

Version 0.15 removed the default UserProfile from the assetcloud code, replacing it with an abstract BaseUserProfile to
allow custom profiles between apps.

* If you are upgrading from an earlier version and planning to upgrade to 2.0.0, it is advised NOT to create the user profiles
before updating to version 2.0.0, or at least postpone committing your UserProfile migrations so that you can recreate them
instead of migrating primary keys! *

To use it create a model extending the BaseUserProfile in your project's main app and add the following line in
settings.py:

    AUTH_PROFILE_MODULE="my_app_name.MyUserProfileModel"

You need to have this option for assetcloud to work, and your UserProfile must extend BaseUserProfile. The simplest
implementation of a UserProfile model would be:

    class MyUserProfileModel(BaseUserProfile):
        pass

You will also need to migrate any existing user profiles to your new profile class so you will need a data migration similar to this:

    class Migration(DataMigration):

        needed_by = (
            ('assetcloud', '0061_auto__del_userprofile'),
        )

        def forwards(self, orm):

            old_profiles = orm['assetcloud.userprofile'].objects.all()

            for old_profile in old_profiles:
                new_profile = orm['assetcloud_example.UserProfile']()
                new_profile.__dict__.update(old_profile.__dict__)
                new_profile.save()

It is important to add the needed_by dependency to have this migration run before the migration which deletes the existing user profiles the existing user profiles.
You will need to manually copy the models dict entry for 'assetcloud.userprofile' from `0060_auto__chg_field_account_storage.py` (the last migration containing assetcloud.userprofile) to this migration to avoid the error `KeyError: "The model 'userprofile' from the app 'assetcloud' is not available in this migration."*`

Upgrading to version 2.2.0 and above
------------------------------------

If you were relying on assetcloud's git_tag method in your fabfiles, you will now need to add a new environment variable in your fabfile to define which applications the tests should run against

    env.test_apps = ['apps', 'assetcloud_example']


Upgrading to version 2.x.x and above
-------------------------

### Django 1.6 Transactions

You need to change any fixture references in migrations from relative paths to absolute paths.

You will also need to remove the following item from the Django Middleware classes in the settings file:

    'django.middleware.transaction.TransactionMiddleware',

and replace it with this:

    ATOMIC_REQUESTS = True

See https://docs.djangoproject.com/en/1.6/topics/db/transactions/#transaction-middleware for more details.

### Upgrade Haystack

In addtion to the above changes, you will need to replace the existing Haystack configuration with the new Haystack 2.x approach, see:

    http://django-haystack.readthedocs.org/en/latest/migration_from_1_to_2.html
    
Specifically make sure you upgrade your old style configurations
    
    HAYSTACK_SEARCH_ENGINE = 'solr'
    HAYSTACK_SOLR_URL = 'http://localhost:9001/solr/default'

to the new style configuration

    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
            'URL': 'http://localhost:9001/solr/default',
            'TIMEOUT': 60 * 5,
            'INCLUDE_SPELLING': True,
            'BATCH_SIZE': 100,
        },
    }
    
Make sure to upgrade your local configuration files

If you are conditionally using settings in your testing configuration you can use something like:

    if HAYSTACK_CONNECTIONS['default']['ENGINE'] == 'haystack.backends.whoosh_backend.WhooshEngine':
        HAYSTACK_CONNECTIONS['default']['PATH'] = os.path.join(TESTING_TEMP_DIR, 'databases/index.whoosh')
    elif HAYSTACK_CONNECTIONS['default']['ENGINE'] == 'haystack.backends.solr_backend.SolrEngine':
        # Replace the last element of the URL with 'test'
        # For example 'http://plumpton:8280/solr/main' will be changed to
        # 'http://plumpton:8280/solr/test'
        url_components = HAYSTACK_CONNECTIONS['default']['URL'].split('/')
        url_components[-1] = 'test'
        HAYSTACK_CONNECTIONS['default']['URL'] = '/'.join(url_components)
    
To use our queued index processor you will need to add the setting:

    HAYSTACK_SIGNAL_PROCESSOR = "assetcloud.search_indexes.AssetQueuedSignalProcessor"

### Upgrade Taggit

Version 2.0.0 introduced support for Django 1.6.8 and included various other package upgrades to support this version of Django. As part of an upgrade to django-taggit,
it is necessary to add the following snippet to the common settings file for the project:

    SOUTH_MIGRATION_MODULES = {
        'taggit': 'taggit.south_migrations',
    }

It is also necessary to run the following command to ensure the correct operation of south migrations:

    python manage.py migrate taggit --fake 0001
    
For rollouts you can do something in the lines of:
    
    with cd(get_vhost_dir()):
    
        def get_version(package):
            version = run('. activate; pip freeze | grep ' + package)
            if "==" in version:
                return version.split("==")[1]
                
        previous_taggit_version = get_version('django-taggit')
        
        ... run the virtual env commands to rebuild ...
        
        new_taggit_version = get_version('django-taggit')
        
        ... then before running the migrations ...
        
        if StrictVersion(previous_taggit_version) < StrictVersion('0.10.0') <= StrictVersion(new_taggit_version):
            run('. activate; ./manage migrate taggit 0001 --fake')

### Upgrade Social auth

Similar to taggit, social auth introduced migrations in v0.7.18 and the first one needs to be faked:

It is also necessary to run the following command to ensure the correct operation of south migrations:

    python manage.py migrate social_auth --fake 0001
    
For rollouts you can do something in the lines of:
    
    with cd(get_vhost_dir()):
    
        def get_version(package):
            version = run('. activate; pip freeze | grep ' + package)
            if "==" in version:
                return version.split("==")[1]
                
        previous_social_auth_version = get_version('django-social-auth')
        
        ... run the virtual env commands to rebuild ...
        
        new_social_auth_version = get_version('django-social-auth')
        
        ... then before running the migrations ...
        
        if StrictVersion(previous_social_auth_version) < StrictVersion('0.7.18') <= StrictVersion(new_social_auth_version):
            run('. activate; ./manage migrate social_auth 0001 --fake')


### Re-instate Ids in User Profiles

If you are upgrading from version 0.15.x or newer, you will have to execute another migration in the user profiles to
reintroduce the id field (Removed when factoring out User Profiles).

To do so run the following:

    ./manage schemamigration your_app_name --auto

When asked, just add any value to use as default and then edit the migration as follows (Only tnabot should needto do 
this tested on mysql, sqlite and postgres):

    def forwards(self, orm):

        try:
            db.delete_foreign_key(u'tnabot_subscription', u'user_profile_id')
            db.delete_foreign_key(u'tnabot_userprofile', u'user_id')
        except Exception:
            pass

        db.delete_primary_key(u'tnabot_userprofile')

        # Adding field 'UserProfile.id'
        if db.backend_name == 'mysql':
            db.add_column(u'tnabot_userprofile', u'id',
                          self.gf('django.db.models.fields.AutoField')(primary_key=True),
                          keep_default=False)
            db.execute('ALTER TABLE `tnabot`.`tnabot_userprofile` CHANGE COLUMN `id` `id` INT(11) NOT NULL AUTO_INCREMENT')
        elif db.backend_name == 'sqlite3':
            db.add_column(u'tnabot_userprofile', u'id',
                            self.gf('django.db.models.fields.AutoField')(primary_key=True, default=0),
                            keep_default=False)
            db.execute('UPDATE tnabot_userprofile SET id = user_id')
            db.create_primary_key(u'tnabot_userprofile', u'id')
        elif db.backend_name == 'postgres':
            db.start_transaction()
            db.add_column(u'tnabot_userprofile', u'id',
                            self.gf('django.db.models.fields.IntegerField')(null=True),
                            keep_default=False)
            db.execute('CREATE SEQUENCE tnabot_userprofile_id_seq')
            db.execute('SELECT setval(\'tnabot_userprofile_id_seq\', max(user_id) + 1) FROM tnabot_userprofile')
            db.commit_transaction()
            db.start_transaction()
            db.execute('UPDATE tnabot_userprofile SET id = user_id')
            db.commit_transaction()
            db.execute('ALTER TABLE tnabot_userprofile ALTER COLUMN id SET DEFAULT nextval(\'tnabot_userprofile_id_seq\')')
            db.create_primary_key(u'tnabot_userprofile', u'id')

        # Changing field 'UserProfile.user'
        db.alter_column(u'tnabot_userprofile', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User']))

        db.foreign_key_sql(u'tnabot_subscription', u'user_profile_id', u'tnabot_userprofile', u'id')
        db.foreign_key_sql(u'tnabot_userprofile', u'user_id', u'auth_user', u'id')

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

### Make sure you are testing all the needed apps

Change your jenkins configuration to specify which tests you want to be running. If you want to run the assetcloud tests
along with yours, you will need to specify it in the test command.

You will also need to change these in your fabfile.py

### Upgrade Solr (if version < 3.6.2)

You will need to make sure that you are using solr version 3.6.2 for wildcard searches to work.

    cd path/to/get/solr
    wget http://archive.apache.org/dist/lucene/solr/3.6.2/apache-solr-3.6.2.tgz
    tar -xvf apache-solr-3.6.2.tgz

If you are on a development environment change ~/.fabricrc if you are on a dev environment

    solr_config=/home/gg/Apps/apache-solr-3.6.2/example

On your servers you will need to undeploy the previous solr and do the following as root

    cd apache-solr-3.6.2
    cp dist/apache-solr-3.6.2.war /var/lib/tomcat6/webapps/solr.war
    chown tomcat6:tomcat6 /var/lib/tomcat6/webapps/solr.war

Copy the contents of example/solr to your new solr home (eg /var/lib/jenkins/assetcloud-solr)

    cp -r example/solr/* /var/lib/jenkins/assetcloud-solr
    
Then in tomcat manager deploy the app using /solr context path and point to the solr war file.

If needed, update the solr home directory in /etc/default/tomcat6

    JAVA_OPTS="$JAVA_OPTS -Dsolr.solr.home=/var/lib/jenkins/assetcloud-solr"

### Remove ignoretests requirements and settings

Django 1.6 uses an inclusive test runner which means that you need to define which apps to run the tests on so you don't
need to have excluded apps.

Delete

    TEST_RUNNER="ignoretests.DjangoIgnoreTestSuiteRunner"

and

    IGNORE_TESTS = (
        'django.contrib.auth',
        'django.contrib.messages',
        'polymorphic'
    )

### Account for \xa0 characters in tests

In Django 1.6 filters add \xa0 instead of ' ' in filters. If you have tests which check for that, make sure to update 
them


Database Migrations
-------------------

Check out the South [documentation](http://south.aeracode.org/docs/) and [tutorial](http://south.aeracode.org/docs/tutorial/index.html)

To create a new migration after changing models.py:

    ./manage schemamigration assetcloud --auto

To apply new migrations:

    ./manage syncdb --migrate

To list all migrations (and see which have not yet been applied):

    ./manage migrate --list


Solr Setup
----------

We have two available search backends: Whoosh for development and Solr for production.  Whoosh is sometimes useful for development, as it works out-of-the-box, but Solr is *much* faster, and supports more functionality.

*Note:* at the moment some functionality (e.g. filtering searches by date range) doesn't work with Whoosh, so it's highly recommended that you use Solr.

Install Solr on Mac OS X, with the following:

	mkdir -p /Applications/Developer
	cd /Applications/Developer
	curl -O http://archive.apache.org/dist/lucene/solr/3.6.2/apache-solr-3.6.2.tgz
	tar zxvf apache-solr-3.6.2.tgz

Then change directory back to your assetcloud project directory.

You can now update your local settings, and start the Solr server:

	echo "HAYSTACK_SEARCH_ENGINE = 'solr'" >> project/settings/local_common.py
	echo "HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr/main'" >> project/settings/local_common.py

	. ./activate
    fab start_solr

If you are switching an existing Asset Cloud instance to Solr then you'll need to build the index:

    ./manage rebuild_index

You'll need Solr to be running whenever you use `./manage runserver` or `./manage test`.  Your tests should run *much* quicker, and some search functionality will work in slightly more sensible ways.

Also note that you'll need to restart Solr if the [search indexes](https://github.com/brightinteractive/assetcloud/blob/master/apps/assetcloud/search_indexes.py) get updated.

For more details, including Solr on the test server, see [the wiki](http://wiki.bright-interactive.com/display/knowhow/Configuring+Asset+Cloud+to+use+the+Solr+Search+Engine).

Using S3 Storage
----------------

S3 storage is enabled by default by the following settings in
project/settings/common.py:

    # Custom assetcloud setting which controls the backend used for Asset Uploads
    ASSET_FILE_STORAGE = 'assetcloud.storage.S3BotoStorage'

    # Settings used by the 'storages' app for the 'S3BotoStorage' backend
    AWS_ACCESS_KEY_ID = ...
    AWS_SECRET_ACCESS_KEY = ...
    AWS_STORAGE_BUCKET_NAME = 'assetcloud-test'

Directly uploading to S3 and having to pull images from S3 everytime we want
to generate thumbnails is potentially bad for performance. We may eventually use a composite storage backend, which would use an S3 storage backend for persistence, and a local file storage backend for performance.

We would use django-celery to periodically clean the local cache.

Publishing
----------

AssetCloud is published on localshop.bright-interactive.com.

Follow the [instructions](https://wiki.bright-interactive.com/display/knowhow/Bright+Interactive+Python+Package+Index+%28Localshop+on+Gold%29) on setting up a new user account on the localhsop.

To create a tag and publish to localshop, run:

	fab tag_and_publish:tag=v0.2.0

(replacing v0.2.0 with the version number you wish to use for the tag - see [http://semver.org/] for rules about version numbers).

Creating a tag will need a matching asset cloud package version in apps/assetcloud/__init__.py

Publishing the current version can be done by running

    python setup.py publish

Continuous Integration
----------------------

[Continuous Integration results](http://plumpton:8080/job/AssetCloud/) are built using Hudson, on plumpton.

One gotcha is that if you update the search indexes, you'll need to make sure you restart Solr (See above) after the first subsequent test run fails.

General Notes
-------------

Using git from the command line is fine, but you'll probably also want GitHub's rather excellent [GitHub for Mac](http://mac.github.com/) tool.

This `README.markdown` file uses [markdown syntax](http://daringfireball.net/projects/markdown/syntax).  There is a great markdown editor for Mac, [Mou](http://mouapp.com/), which you might find useful.

For development Asset Cloud uses a SQLite database, for ease of use. [Base](http://menial.co.uk/software/base/) is really nice sqlite database tool (again for Mac).

If you want to use PostgreSQL instead make sure that you use psycopg2 version 2.4.1 because version 2.4.2 is incompatible with Django 1.3. In deployment environments, to get dbbackup to work (and if you're not using ident authentication) then you need to create a .pgpass file in the bright user's home directory. This should contain the password for the database in question.


Developing apps which use AssetCloud
====================================


Choosing a version for AssetCloud development
---------------------------------------------

Since version 1.0.0 we started using a Semantic Versioning scheme with pre-release extensions.

http://semver.org/spec/v2.0.0.html

Backwards incompatible changes should bump the major version
Backwards compatible changes should bump the minor version
Fixes should bump the patch version unless they introduce backwards incompatibilies, in which case they should bump the major version
Development should be done using the pre-release extensions in a new version (backwards compatible or not)


AssetCloud public API
---------------------

We don't have a well-defined API so we consider the API to basically be "any part of the app which was used in an
external app" and "things which require changes in dependant apps"

These are likely to be backwards incompatible changes:
(Update this list when you come across something which applies here)

  1. Defining new settings with no default values.
  2. Changing a contract test

Note that solely relying on this list is very optimistic. If a change is obviously backwards incompatible it should be
treated as such.

Claiming parts of the app as API
--------------------------------

As mentioned above, there is no strict definition of a public API for assetcloud, so to prevent your app from breaking
with assetcloud updates we have introduced contract tests.

These are tests which should be considered as vital for the app which is claiming them, meaning that any change to these
tests should be considered unsafe and should be done with caution. Failures in these tests probably also mean that the
claiming app will break.

There are two ways to define a contract test:

 1. Add some test suites in assetcloud/tests/contract/ making the name of the dependant app clear.
 2. Decorate any existing test with the ContractTest decorator defining the dependant app name in the app parameter. Note
 that you should decorate a test even if has already been decorated by another application, by adding another decorator.

 | @ContractTest(app="tnabot")

This should act as a guarantee that your app will not be breaking without warning because of an assetcloud version update.

Writing contract tests
----------------------

The general recommendation is writing a test for every part of assetcloud you are using in the dependant app. This can be
use of models, utility functions, overriding templates and views, imports etc.

If there are no tests in assetcloud to preserve the functionality you are using, either create one in the general assetcloud
test folders and decorate it as a ContractTest or create one in assetcloud's contract test folder.

Remember that the more tests you write, the more guaranteed you are to have the used functionality preserved with assetcloud
updates.

There is a helper ContractTestCase with some useful asserts to make this process easier.

Failing contract tests
----------------------

If a test within /assetcloud/tests/contracts or a ContractTest fails during development, then proceed with caution. Changing
the test to fix the failure could cause Bad Things to the dependant app. It should be obvious which app depends on the
test so you should be able to see how this test will affect it. If in doubt, ask one of the developers of the dependent
app.

Nonetheless, if there need to be changes to any one of these tests, then the change should be considered backwards
incompatible and the version change should represent that with a major version iteration. The change should be documented
for the developers who will be updating the dependant app.


Publishing Releases to Localshop
================================

First make sure you have created a user and set up access to http://localshop.bright-interactive.com by following the instructions in https://wiki.bright-interactive.com/display/knowhow/Bright+Interactive+Python+Package+Index+(Localshop+on+Gold).

Set the `__version__` string in `apps/assetcloud/__init__.py`, commit this change, push it and then run:

    # Run the tests - do not publish if the tests fail or you haven't/can't run them
    ./manage test apps assetcloud_example
    # Publish to localshop
    ./setup.py publish
    # Tag (change 1.0.0 to the version you are publishing!)
	git tag -a v1.0.0 -m 'Version 1.0.0'
	git push --tags

	or

	fab tag_and_publish:v1.0.0

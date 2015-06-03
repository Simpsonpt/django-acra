#Django-ACRA
####Ready To Go Helper!

Django Model, View and Admin Panel for ACRA (Application Crash Reports for Android).


##Installation

Assuming that the project name is **my_android_server** copy the folder **acra** to the project and then edit **settings.py** and **urls.py**.



- In the **settings.py** file just add:

```
INSTALLED_APPS = (
    'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
    '...'
	'my_android_server.acra',
)
```

 - In the **urls.py** make sure to include this:

```
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
import settings

urlpatterns = patterns('',
    ...
	url(r'^acra/', include("my_android_server.acra.urls")),
	url(r'^admin/', include(admin.site.urls)),
    ...
)
```

- Finally **sync** the database

```
$ python manage.py syncdb
```

- Create a Django user in your admin page (to get a `username` and `password`) and set the acra permissions(`'acra.add_crashreport'`, `'acra.change_crashreport'` and `'acra.delete_crashreport'`) to this new user.

##Android Snippet

- Application Class

```
package com.pathonproject.testacra;

import org.acra.ACRA;
import org.acra.annotation.ReportsCrashes;

import android.app.Application;

@ReportsCrashes(
        formUri = "http://pathonproject.com/acra/"),
        reportType = HttpSender.Type.JSON,
        formUriBasicAuthLogin = "<username>",
        formUriBasicAuthPassword = "<password>"
)
public class TA extends Application
{

	public void onCreate()
	{
	    super.onCreate();
	    ACRA.init(this);
	    
	    //ACRA.getErrorReporter().handleException(null);
	    ACRA.getErrorReporter().checkReportsOnApplicationStart();
	    //ACRA.getErrorReporter().handleException(null);
	}
}
```

- AndroidManifest.xml

``` 
    <!-- Debug Acra -->
    <uses-permission android:name="android.permission.READ_LOGS"></uses-permission>
    
    <application
        android:allowBackup="false"
        android:icon="@drawable/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.Sherlock.Light.DarkActionBar" 
        android:name="com.pathonproject.testacra.TA">
        <activity
            android:name="com.pathonproject.testacra.Init"
            android:label="@string/app_name"
            android:noHistory="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
```

##Screenshot

![Screenshot](https://raw.github.com/Simpsonpt/django-acra/master/Screenshot.png)
 
##Version

* [Django ACRA v1.0]

##Tech

* [ACRA] - Application Crash Reports for Android
* [License] - Module License

##Author

* [@Simps0n] - Twitter
* [Pathon Project Playground] - Webpage

  [ACRA]: https://github.com/ACRA/acra   
  [License]: https://github.com/Simpsonpt/django-acra/blob/master/LICENSE    
  [Django ACRA v1.0]: https://github.com/Simpsonpt/django-acra/releases/tag/django-acra-1.0
  [@Simps0n]: https://twitter.com/simps0n
  [Pathon Project Playground]: http://www.pathonproject.com/

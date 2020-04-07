Windows Dev Notes
====================

.. note::

    David Chen wrote this up for use on his Windows box. Your situation may be different, but hopefully this is useful to you.

Notes for Windows users
-----------------------

Install Bash: https://msdn.microsoft.com/en-us/commandline/wsl/about

After installing Bash and setting up your user:

::

    apt-get install make

These instructions may help you get docker working with Bash for
Windows:

::

    https://blog.jayway.com/2017/04/19/running-docker-on-bash-on-windows/


Further instructions for Windows users (updated July 5, 2017)
-------------------------------------------------------------

Note: These instructions were tested for
``Docker version 17.05.0-ce, build 89658be`` and
``docker-compose version 1.14.0, build c7bdf9e``.

0.  Install Bash for Windows using the instructions above
1.  Install Docker CE for Windows and run it:
    https://store.docker.com/editions/community/docker-ce-desktop-windows

2.  Right-click on Docker in your system tray, and click on
    **Settings**.
3.  In the **General** tab, check **Expose daemon on
    tcp://localhost:2375 without TLS**.
4.  In the **Shared Drives** tab, check on the local drive (usually
    drive C) and click **Apply**. If the settings are not saved after
    clicking apply, see below. Else, continue.

    -  If your drive simply refuses to be checked, it may have to do
       with the sharing permissions allowed on your account (this seems
       to be the problem for Microsoft Azure AD accounts).
    -  A workaround:

       -  **Windows Menu > Administrative Tools > Computer Management >
          System Tools > Local Users and Groups > Users**
       -  On the top menu, click **Actions > New User...**. Set both
          username and password to "docker" (or whatever you'd like)
       -  Uncheck **User must change password at next logon** and check
          **Password never expires**
       -  Switch to this new account and try to access your main files
          in **C:/Users/your-username**, which will prompt you to
          authenticate with your username and password
       -  Once authenticated, switch back to your main account (do not
          log out of the docker account) and try the step above **but
          using the credentials of the new account** (see image below):

       -  If issue persists, check the Docker logs by clicking on the
          **Diagnose and Feedback** tab and selecting **log file**, or
          open an issue here on Github

5.  Open a Windows command line and run ``bash`` - you should now be in
    a Bash shell
6.  Elevate permission to install the newest version of Docker by
    running ``sudo chown -R {$USERNAME} /usr/local/bin`` and replace
    ``{$USERNAME}`` with your username
7.  Install Docker 17.05.0 using
    ``curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-17.05.0-ce.tgz && tar --strip-components=1 -xvzf docker-17.05.0-ce.tgz -C /usr/local/bin``
8.  Install docker-compose using ``sudo apt install docker-compose``
9.  Run ``docker --version`` to check your version is ``>= 17.05.0``
    after the above installation
10. If not already in the Desktop directory,
    ``cd /mnt/{$DRIVE-LETTER}/Users/{$USERNAME}/Desktop/``. For example,
    mine was ``/mnt/c/Users/DavidChen/Desktop/``
11. ``git clone git@github.com:belbio/bel_api.git``
12. ``cd bel_api/``
13. ``cp api/Config.yml.sample api/Config.yml`` and edit Config.yml if
    necessary.
14. ``docker-compose start``
15. The services should now be up and ready.
16. Run ``docker-compose logs -f`` to view logs. Run
    ``docker-compose stop`` to stop all services.



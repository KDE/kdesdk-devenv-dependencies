# Creating an environment

This package's main role is to point to the modules that will be required for comfortable development of both KDE applications and extending the Plasma shell.

In itself it won't be providing anything but specify a set of resources that we need to make sure they're installed.

## Developers

If you're here it's because you want to work on KDE Software or extend it. Here we provide a script named `packages` that will install the required software for your system to be able to develop most KDE Software. Some applications will have specific needs, here we are trying to address the general case.

Once the required software is installed, you'll be able to clone and compile the project you have in mind. Here's some documentation on the next steps:
[https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source](https://community.kde.org/Guidelines_and_HOWTOs/Build_from_source)

## Distributions

If you're here it's because you want to provide a package that will help the users of your distribution to contribute to KDE. Thank you!
To that end you'll be providing a meta-package with the information this is giving you. This is not a normal package.
This meta-package will provide the Appstream information that can be found in this directory as well as the dependencies that the `packages` script outputs.

# Help

If none of this is helping you, please contact us at kde-devel@kde.org.

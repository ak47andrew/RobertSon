import argostranslate.package

# Update the package index
argostranslate.package.update_package_index()

# Get the available packages
available_packages = argostranslate.package.get_available_packages()

# Iterate through the available packages and install them
for package_to_install in available_packages:
    # Print a message indicating the installation of the package
    print(f"Installing package {package_to_install}")
    # Download the package
    z = package_to_install.download()
    # Print a message indicating that the package has been downloaded
    print(f"Downloaded package {package_to_install}")
    # Install the package from the downloaded path
    argostranslate.package.install_from_path(z)
    # Print a message indicating that the package has been installed
    print(f"Installed package {package_to_install}")
    # Print a separator line
    print("-----")

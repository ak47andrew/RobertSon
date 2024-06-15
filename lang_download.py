import argostranslate.package

argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

for package_to_install in available_packages:
    print(f"Installing package {package_to_install}")
    z = package_to_install.download()
    print(f"Downloaded package {package_to_install}")
    argostranslate.package.install_from_path(z)
    print(f"Installed package {package_to_install}")
    print("-----")

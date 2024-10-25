# Dynamically determine the project name from the current directory
REPO_URL="https://github.com/Ripax/Authenticator.git"
PROJECT_NAME = $(shell basename $(CURDIR) | sed 's/-/_/g')
.TEMP = $(HOME)/.tmp
SOURCE_DIR = .
VERSION_FILE = $(SOURCE_DIR)/__version__
INSTALL_VERSION = $(shell cat $(VERSION_FILE) 2>/dev/null)
SOFTWARE_DIR = $(SOFTWARE)
INSTALL_DIR = $(SOFTWARE_DIR)/$(PROJECT_NAME)

VERSION ?= $(version)

# Define the installation target
install: pre_install copy_files clean_hidden hidden_update
	@echo "version path: $(INSTALL_DIR)/$(INSTALL_VERSION)"
	@echo "Installing version: $(VERSION)"
	@echo "Installed version: $(INSTALL_VERSION)"
	@notify-send -i /home/rion/dev/nuke-tools/icons/Skull-icon.png "Installation Completed" "Tool: $(PROJECT_NAME)\nVersion: $(VERSION)"

pre_install:
	@if [ ! -d "$(.TEMP)" ]; then \
		echo "Creating temp directory."; \
		mkdir -p "$(.TEMP)"; \
	fi

	@if [ ! -d "$(.TEMP)/.git" ]; then \
		echo "Cloning repository..."; \
		git clone "$(REPO_URL)" "$(.TEMP)"; \
	else \
		echo "Repository already exists. Pulling the latest changes..."; \
		git -C "$(.TEMP)" pull; \
	fi

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@echo "  install        Install the tool, copying files and updating init.py."
	@echo "  pre_install    Check if the version is specified and compare installed versions."
	@echo "  copy_files     Copy files to the version directory."
	@echo "  update_init    Update the init.py file with the new plugin path."
	@echo "  clean_hidden   Clean hidden folders and __pycache__ directories."
	@echo "  check_version  Display the current version from the version file."
	@echo "  update         Update the tool, invoking install."
	@echo "  clean          Clean up the installation of the tool."
	@echo "  all            Default target, equivalent to 'install'."

test:
	@echo "Version: $(INSTALL_VERSION)"
	@echo "Software dir: $(SOFTWARE_DIR)"
	@echo "Install Dir: $(INSTALL_DIR)"

copy_files:
	@mkdir -p -v $(INSTALL_DIR)/$(VERSION)
	@cp -rv $(SOURCE_DIR)/* $(INSTALL_DIR)/$(VERSION)
	@mv -v $(INSTALL_DIR)/$(VERSION)/__version__ $(INSTALL_DIR)/$(VERSION)/.version
	@echo "Files copied to $(INSTALL_DIR)/$(VERSION)."

update:
	@echo "Initializing the update from the repo..."
	@$(MAKE) copy_files
	@$(MAKE) install
	@echo "Update completed."

clean:
	@if [ -z "$(VERSION)" ]; then \
		echo "Error: VERSION is not specified. Usage: make clean version=<VERSION>"; \
		exit 1; \
	fi
	rm -rf $(INSTALL_DIR)/$(VERSION)

clean_hidden:
	@echo "Cleaning unwanted files and folders..."
	rm -rf $(.TEMP)
	@if [ -d "$(INSTALL_DIR)" ]; then \
		echo "Cleaning the $(PROJECT_NAME)..."; \
		find "$(INSTALL_DIR)/$(VERSION)" -type d -name '.*' -exec rm -rf {} +; \
		find "$(INSTALL_DIR)/$(VERSION)" -type d -name '__pycache__' -exec rm -rf {} +; \
		find "$(INSTALL_DIR)/$(VERSION)" -type f -name '__version__' -exec rm -rf {} +; \
		find "$(INSTALL_DIR)/$(VERSION)" -type f -name 'LICENSE.txt' -exec rm -rf {} +; \
		find "$(INSTALL_DIR)/$(VERSION)" -type f -name 'README.md' -exec rm -rf {} +; \
		find "$(INSTALL_DIR)/$(VERSION)" -type f -name 'Makefile' -exec rm -rf {} +; \
		find "$(INSTALL_DIR)/$(VERSION)" -type l ! -exec test -e {} \; -exec rm -f {} +; \
		echo "Installed version is: $(INSTALL_VERSION)"; \
		echo "$(PROJECT_NAME) cleaned successfully."; \
	else \
		echo "$(PROJECT_NAME) is not installed."; \
	fi

hidden_update:
	@echo "$(INSTALL_VERSION)" > $(INSTALL_DIR)/$(VERSION)/.version

uninstall:
	@read -p "What! Really do you want to uninstall the $(PROJECT_NAME)? (y/n): " choice; \
	if [ "$$choice" = "y" ]; then \
		if [ -d "$(INSTALL_DIR)" ]; then \
			echo "Uninstalling $(PROJECT_NAME)..."; \
			rm -rf $(INSTALL_DIR); \
			echo "$(PROJECT_NAME) uninstalled."; \
		else \
			echo "$(PROJECT_NAME) is not installed."; \
		fi \
	else \
		echo "Uninstall aborted."; \
	fi

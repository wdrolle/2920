
# Installing MongoDB on Ubuntu 22.04.3 LTS

MongoDB is not officially supported on Ubuntu 22.04 yet, but you can follow these steps to install it with a workaround.

1. **SSH into your Ubuntu Server:**

    ```bash
    ssh your_username@your_server_ip
    ```

2. **Update Your Package List:**

    ```bash
    sudo apt update
    ```

3. **Install libssl1.1:**

    Ubuntu 22.04 requires an older version of `libssl1.1`. Download it from the official repository and install it:

    ```bash
    wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.1f-1ubuntu2_amd64.deb
    sudo dpkg -i libssl1.1_1.1.1f-1ubuntu2_amd64.deb
    ```

4. **Proceed with the installation of MongoDB:**

    ```bash
    sudo apt-get install -y mongodb-org
    ```

5. **Start MongoDB:**

    ```bash
    sudo service mongod start
    ```

6. **Enable MongoDB to Start on Boot:**

    ```bash
    sudo systemctl enable mongod
    ```

7. **Verify MongoDB Installation:**

    ```bash
    sudo service mongod status
    ```

8. **Access the MongoDB Shell:**

    You can access the MongoDB shell by running:

    ```bash
    mongo
    ```

These steps should help you install MongoDB on your Ubuntu 22.04.3 LTS server.

# Merging Client and Server `package.json` Files into Root Level `package.json`

## Step 1: Initialize `package.json` at the Root Level
Navigate to the root of your `Blog-Website` directory and initialize a new `package.json` file.

```bash
cd ~/Blog-Website
npm init -y
```

## Step 2: Merge Dependencies
Combine the dependencies from both `client/package.json` and `server/package.json` into the root `package.json`. Check for any version conflicts and resolve them.

**Root `package.json` (Add the dependencies section):**

```json
"dependencies": {
    "@emotion/react": "^11.9.0",
    "@emotion/styled": "^11.8.1",
    "@mui/icons-material": "^5.8.0",
    "@mui/material": "^5.8.0",
    "@testing-library/jest-dom": "^5.14.1",
    "@testing-library/react": "^11.2.7",
    "@testing-library/user-event": "^12.8.3",
    "axios": "^0.21.1",
    "bcrypt": "^5.0.1",
    "body-parser": "^1.20.0",
    "cors": "^2.8.5",
    "dotenv": "^16.0.1",
    "express": "^4.18.1",
    "gridfs-stream": "^1.1.1",
    "jsonwebtoken": "^8.5.1",
    "mongoose": "^6.3.4",
    "multer": "^1.4.4",
    "multer-gridfs-storage": "^5.0.2",
    "nodemon": "^2.0.16",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-router-dom": "^6.3.0",
    "react-scripts": "4.0.3",
    "web-vitals": "^1.1.2"
  }
```

## Step 3: Merge Scripts
Update the scripts in the root `package.json` to include the scripts from both client and server. Use `concurrently` to run both client and server scripts.

**Root `package.json` (Add the scripts section):**

```json
"scripts": {
    "start": "concurrently \"cd client && npm start\" \"cd server && npm start\"",
    "test": "echo \"Error: no test specified\" && exit 1",
    "client-start": "cd client && react-scripts start",
    "client-build": "cd client && react-scripts build",
    "client-test": "cd client && react-scripts test",
    "client-eject": "cd client && react-scripts eject",
    "server-start": "cd server && nodemon index.js"
  }
```

## Step 4: Install Concurrently
Install `concurrently` to run multiple commands simultaneously.

```bash
npm install concurrently --save-dev
```

## Step 5: Install Dependencies
Run `npm install` at the root level to install all combined dependencies.

```bash
npm install
```

## Step 6: Start the Application
Now, you can start both the client and server by running the start script from the root of your project.

```bash
npm start
```

**Note:** Make sure to test the application thoroughly to ensure both client and server are functioning correctly after these changes.

---

# Installing NVM and Node.js v16

## Install NVM (Node Version Manager)
NVM allows you to easily switch between Node.js versions. Install it with:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```

## Load NVM
To start using NVM, either restart your terminal or run:

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

## Install Node.js Version 16
Once NVM is installed, install Node.js version 16:

```bash
nvm install 16
nvm use 16
```

## Verify Node.js Installation
Check your Node.js version to ensure you're using version 16:

```bash
node --version
```

## Uninstalling a Node.js Version (Optional)
If you need to uninstall a specific Node.js version (e.g., v21.6.0) installed via NVM:

```bash
nvm uninstall 21.6.0
```

Verify the uninstallation by listing all installed Node.js versions:

```bash
nvm ls
```

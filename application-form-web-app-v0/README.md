# Application Form Web App

## 1. Prerequisites

Make sure you have installed:

- Node.js (v18+)
- npm or yarn
- MongoDB (either locally or via MongoDB Atlas)

## 2. Clone Your Project Repository

```PowerShell
cd <project_repository>
npm init -y
```

This creates a new Node project with a default package.json.

## 3. Install Dependencies

You’ll need:
Express → web framework for the backend
Mongoose → MongoDB object modeling
dotenv → for environment variables
cors → to allow your frontend to connect
nodemon → for auto-restarts in dev mode

npm install express mongoose dotenv cors
npm install --save-dev nodemon

## Step 4

Start the MongoDB server

```PowerShell
# To start mongodb server
mongod --dbpath <your_path>

# To connect to server
# don’t close the one running `mongod` and open a new terminal.
mongosh
```

## 5. Configure .env

Inside .env:

```text
PORT=5000 <--(has set defult to 5000)
MONGODB_URI=<mongodb connection url>
```

Same has been .itignore along with  "node_modules/"

## 6. Test Everything

Run your backend → npm run dev

Visit <http://localhost:5000> — you should see: "Hello from the backend!"

Open frontend/index.html in browser

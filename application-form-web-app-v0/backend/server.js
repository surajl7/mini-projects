import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import userRoutes from "./routes/users.js";
import dotenv from "dotenv";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI)
  .then(() => console.log("✅ MongoDB connected"))
  .catch(err => console.error(err));

app.use("/api/users", userRoutes);

// Example route
app.get("/", (req, res) => {
  res.send("Hello from backend!");
});

// Start server
app.listen(5000, () => console.log("Server running on port 5000"));

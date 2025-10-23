import express from "express";
import User from "../models/userModel.js";

const router = express.Router();

// Create user
router.post("/", async (req, res) => {
  const user = new User(req.body);
  await user.save();
  res.json(user);
});

// Get all users
router.get("/", async (req, res) => {
  const users = await User.find();
  res.json(users);
});

export default router;

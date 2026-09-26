const express = require("express");

const {
  createBooking,
  getBookings,
  getUserBookings,
  approveBooking,
  rejectBooking,
  cancelBooking,
} = require("../controllers/bookingController");

const {
  authenticate,
  authorize,
} = require("../middleware/authMiddleware");

const router = express.Router();

// Student and faculty can create bookings
router.post(
  "/",
  authenticate,
  authorize("STUDENT", "FACULTY"),
  createBooking
);

// Admin can see all bookings
router.get(
  "/",
  authenticate,
  authorize("ADMIN"),
  getBookings
);

// Student/faculty can see their bookings
router.get(
  "/user/:userId",
  authenticate,
  getUserBookings
);

// Admin actions
router.put(
  "/:id/approve",
  authenticate,
  authorize("ADMIN"),
  approveBooking
);

router.put(
  "/:id/reject",
  authenticate,
  authorize("ADMIN"),
  rejectBooking
);

// Logged-in users can cancel
router.put(
  "/:id/cancel",
  authenticate,
  authorize("STUDENT", "FACULTY"),
  cancelBooking
);

module.exports = router;
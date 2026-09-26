const express = require("express");

const {
  getFacilities,
  getFacilityById,
  createFacility,
  updateFacility,
  deleteFacility,
} = require("../controllers/facilityController");

const {
  authenticate,
  authorize,
} = require("../middleware/authMiddleware");

const router = express.Router();

// Anyone logged in can view facilities
router.get("/", authenticate, getFacilities);
router.get("/:id", authenticate, getFacilityById);

// Only admin can manage facilities
router.post(
  "/",
  authenticate,
  authorize("ADMIN"),
  createFacility
);

router.put(
  "/:id",
  authenticate,
  authorize("ADMIN"),
  updateFacility
);

router.delete(
  "/:id",
  authenticate,
  authorize("ADMIN"),
  deleteFacility
);

module.exports = router;
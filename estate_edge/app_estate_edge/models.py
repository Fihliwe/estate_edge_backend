from django.db import models

class User(models.Model):
    USER_ROLES = {
        "A": "Admin",
        "L": "Landlord",
        "T": "Tenant"
    }
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    roles = models.CharField(max_length=1, choices=USER_ROLES)

class Property(models.Model):
    property_name = models.CharField(max_length=250)
    property_number = models.IntegerField()
    property_units = models.ImageField()

class Lease(models.Model):
     PAYMENT_STATUS = {
         "P": "Pending",
         "PA": "Paid",
         "O": "Overdue"
     }
     LEASE_STATUS = {
         "A": "Active",
         "E": "Expired",
         "T": "Terminated"
     }
     tenant = models.CharField(max_length=30)
     property = models.CharField(max_length=30)
     start_date = models.DateField()
     end_date = models.DateField()
     rent_amount = models.IntegerField()
     payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS)
     lease_status = models.CharField(max_length=1, choices=LEASE_STATUS)

class Payments(models.Model):
    rent = models.IntegerField()
    maintenance_payment = models.ImageField()


class Maintenance(models.Model):
    MAINTENANCE_REQUESTS = {
        ("emergency_gas_leak", "Gas Leak (Emergency)"),
        ("emergency_electrical_failure", "Electrical Failure (Emergency)"),
        ("emergency_water_leak", "Water Leak / Burst Pipes (Emergency)"),
        ("emergency_fire_damage", "Fire / Smoke Damage (Emergency)"),
        ("emergency_broken_lock", "Broken Lock / Security Issue (Emergency)"),

        ("routine_hvac_service", "HVAC Servicing"),
        ("routine_plumbing_inspection", "Plumbing Inspection"),
        ("routine_roof_cleaning", "Roof & Gutter Cleaning"),
        ("routine_pest_control", "Pest Control"),
        ("routine_smoke_detector_check", "Smoke Detector Check"),

        ("cosmetic_painting", "Painting (Interior / Exterior)"),
        ("cosmetic_wall_crack_repair", "Wall Crack Repair"),
        ("cosmetic_flooring_repair", "Flooring Repair / Replacement"),
        ("cosmetic_fixture_upgrade", "Fixture Upgrade (Lights, Faucets, etc.)"),

        ("structural_foundation_repair", "Foundation Repair"),
        ("structural_roof_repair", "Roof Repair"),
        ("structural_wall_damage", "Wall Damage Repair"),
        ("structural_window_replacement", "Window / Door Frame Replacement"),

        ("appliance_fridge_repair", "Refrigerator Repair / Replacement"),
        ("appliance_oven_repair", "Oven / Stove Repair"),
        ("appliance_water_heater", "Water Heater Repair / Replacement"),
        ("appliance_dishwasher_repair", "Dishwasher Repair"),

        ("electrical_circuit_breaker", "Circuit Breaker Issue"),
        ("electrical_flickering_lights", "Flickering Lights / Dead Outlets"),
        ("plumbing_slow_drain", "Slow Drain / Clogged Pipes"),
        ("plumbing_running_toilet", "Running Toilet / Leaky Faucet"),

        ("tenant_security_upgrade", "Additional Locks / Security Cameras"),
        ("tenant_install_ceiling_fan", "Ceiling Fan Installation"),
        ("tenant_fixture_layout_change", "Fixture Layout Change"),
    }
    STATUS_CODE = {
        "pending": "Pending",
        "in_progress": "In Progress",
        "completed" : "Completed",
        "cancelled": "Cancelled"
    }
    property = models.ForeignKey("Property", on_delete=models.CASCADE)
    request_type = models.CharField(max_length=1, choices=MAINTENANCE_REQUESTS)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status_code = models.Charfiled(max_length=1, choices=STATUS_CODE) 
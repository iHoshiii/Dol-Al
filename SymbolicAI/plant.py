def diagnose_plant():
    print("--- Professional Plant Health Diagnostic Tool ---")
    print("Please answer 'yes' or 'no' to the following symptoms:\n")

    # 1. Fact Gathering (Inputs)
    yellow_leaves = input("Are the leaves turning yellow? ").lower() == 'yes'
    wet_soil = input("Is the soil soaking wet? ").lower() == 'yes'
    dry_soil = input("Is the soil dry/shrinking? ").lower() == 'yes'
    crispy_tips = input("Are the leaf tips brown and crispy? ").lower() == 'yes'
    leaning = input("Is the plant leaning toward a light source? ").lower() == 'yes'
    small_leaves = input("Are new leaves unusually small or pale? ").lower() == 'yes'
    white_clusters = input("Do you see white, cottony clusters? ").lower() == 'yes'
    drooping = input("Is the plant drooping/wilting? ").lower() == 'yes'
    
    # New Facts for expanded rules
    dark_spots = input("Are there soft, dark brown/black spots on leaves? ").lower() == 'yes'
    sticky_residue = input("Is there a sticky substance (honeydew) on leaves? ").lower() == 'yes'
    winter_season = input("Is it currently winter/cold season? ").lower() == 'yes'
    tap_water = input("Do you use unfiltered tap water? ").lower() == 'yes'
    stunted_growth = input("Has growth stopped despite it being growing season? ").lower() == 'yes'

    print("\n--- Final Diagnosis ---")
    results = []
    
    # Rule 1: Standard Overwatering
    if yellow_leaves and wet_soil:
        results.append("Diagnosis: Overwatering. (Action: Reduce watering frequency.)")
    
    # Rule 2: Dehydration
    if crispy_tips and dry_soil:
        results.append("Diagnosis: Under-watering. (Action: Immediate deep watering.)")
    
    # Rule 3: Phototropism (Light hunger)
    if leaning and small_leaves:
        results.append("Diagnosis: Light Deficiency. (Action: Increase light exposure.)")
    
    # Rule 4: Common Pests
    if white_clusters:
        results.append("Diagnosis: Mealybug Infestation. (Action: Use Neem oil.)")
    
    # Rule 5: Critical Root Failure
    if drooping and wet_soil:
        results.append("Diagnosis: Advanced Root Rot. (Action: Inspect roots for mushiness; repot.)")

    # Rule 6: Fungal Infection (New)
    if dark_spots and wet_soil:
        results.append("Diagnosis: Fungal Leaf Spot. (Action: Remove affected leaves; reduce humidity.)")

    # Rule 7: Scale or Aphids (New)
    if sticky_residue:
        results.append("Diagnosis: Sap-sucking Pests (Scale/Aphids). (Action: Wipe leaves with soapy water.)")

    # Rule 8: Dormancy (New)
    if winter_season and stunted_growth:
        results.append("Diagnosis: Natural Dormancy. (Action: Do not fertilize; reduce water until Spring.)")

    # Rule 9: Chemical Sensitivity (New)
    if crispy_tips and tap_water and not dry_soil:
        results.append("Diagnosis: Chlorine/Fluoride Sensitivity. (Action: Use distilled or filtered water.)")

    # Rule 10: Nutrient Depletion (New)
    if yellow_leaves and not wet_soil and stunted_growth:
        results.append("Diagnosis: Nitrogen Deficiency. (Action: Apply a balanced liquid fertilizer.)")

    # 3. Output Handling
    if results:
        for r in results:
            print(f"[*] {r}")
    else:
        print("Result: No clear match found. Your plant might just be dramatic!")

if __name__ == "__main__":
    diagnose_plant()
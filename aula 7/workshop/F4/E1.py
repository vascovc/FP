# coding: utf-8

# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.
def bodyMassIndex(height, weight):
    bmi = weight/(height**2)
    return bmi

# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 
def bmiCategory(bmi):
    # Complete the function definition...
    if bmi < 18.5:
    	return "Underweight"
    elif bmi < 25:
    	return "Normal weight"
    elif bmi < 30:
    	return "Overweight"
    else:
    	return "Obesity"

# This is the main function
def main():
    print("Índice de Massa Corporal")
    altura = float(input("Altura (m)? "))
    peso = float(input("Peso (kg)? "))

    # Complete the function calls...
    imc = bodyMassIndex(altura,peso)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)


# Program starts executing here
main()

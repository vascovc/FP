# coding: utf-8

# This function computes the body mass index (BMI),
# given the height (in meter) and weight (in kg) of a person.
def bodyMassIndex(height, weight):
    # Complete the function definition...
    bmi = weight/height**2
    return bmi


# This function returns the BMI category acording to this table:
# BMI:        <18.5         [18.5, 25[      [25, 30[      30 or greater 
# Category:   Underweight   Normal weight   Overweight    Obesity 
def bmiCategory(height, weight):
    # Complete the function definition...
    bmi = bodyMassIndex(height, weight)
    if bmi < 18.5:
        strSaida = "Underweight"
    elif bmi < 25:
        strSaida = "Normal weight"
    elif bmi < 30:
        strSaida = "Overweight"
    else:
        strSaida = "Obesity"
    return strSaida


# This is the main function
def main():
    print("Índice de Massa Corporal")
    height = float(input("Altura (m)? "))
    weight = float(input("Peso (kg)? "))

    # Complete the function calls...
    imc = bodyMassIndex(height, weight)
    cat = bmiCategory(height, weight)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)


# Program starts executing here
main()

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

if __name__ == "__main__":
    print("Conversor de Temperatura")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Kelvin para Celsius")

    escolha = input("Escolha a conversão (1-4): ")

    try:
        if escolha == "1":
            temp = float(input("Digite a temperatura em Celsius: "))
            print(f"{temp}°C = {celsius_para_fahrenheit(temp):.2f}°F")
        elif escolha == "2":
            temp = float(input("Digite a temperatura em Celsius: "))
            print(f"{temp}°C = {celsius_para_kelvin(temp):.2f}K")
        elif escolha == "3":
            temp = float(input("Digite a temperatura em Fahrenheit: "))
            print(f"{temp}°F = {fahrenheit_para_celsius(temp):.2f}°C")
        elif escolha == "4":
            temp = float(input("Digite a temperatura em Kelvin: "))
            print(f"{temp}K = {kelvin_para_celsius(temp):.2f}°C")
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

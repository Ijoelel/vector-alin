import matplotlib.pyplot as plt
from PIL import Image
from pdf2image import convert_from_path
from math import sqrt, acos

import vector_calc as vc

# local lib
import crop

def formula(name, vector1, vector2 = []):

    def latex_to_png(latex_str):
        fig = plt.figure()

        plt.axis("off")
        plt.text(0.5, 0.5, f"${latex_str}$", size=10, ha="center", va="center")

        pdf_path = f"run/assets/{name}.pdf"
        png_path = f"run/assets/{name}.png"

        plt.savefig(pdf_path, format="pdf", bbox_inches="tight", pad_inches=0.1)
        plt.close(fig)

        images = convert_from_path(pdf_path)
        images[0].save(png_path, "PNG")

        return png_path

    # untuk perhitungan dot
    if name == "dot":

        dot_formula1 = " + ".join([f"(v_{x} \\times w_{y})" for x,y in zip([i for i in range(1, len(vector1) + 1)], [i for i in range(1, len(vector1) + 1)])])
        dot_formula2 = " + ".join([f"({x} \\times {y})" for x,y in zip(vector1, vector2)])
        dot_formula3 = [f"{int(x) * int(y)}" for x,y in zip(vector1, vector2)]
        result = vc.dot(list(map(int, vector1)), list(map(int, vector2)))

        latex_formula = "\\vec{v} \\cdot \\vec{w} = " + f"{dot_formula1}$" + "\n" + "$\\vec{v} \\cdot \\vec{w} = " + f"{dot_formula2}$" + "\n" + "$\\vec{v} \\cdot \\vec{w} = " + f"{' + '.join(dot_formula3)}$" + "\n" + "$\\vec{v} \\cdot \\vec{w} = " + f"{result}"
    
    # untuk perhitungan length
    elif name == "length":

        length_formula1 = " + ".join(f"{{v_{{{x}}}}}^2" for x in [i for i in range(1, len(vector1) + 1)])
        length_formula2 = " + ".join(f"{{{i}}}^2" for i in vector1)
        length_formula3 = [pow(int(i), 2) for i in vector1]

        if vc.length(list(map(int, vector1))) % 1 != 0:
            latex_formula = "||v|| = \\sqrt{v \\cdot v}$" + "\n" + "$||v|| = " + f"\\sqrt{{{length_formula1}}}$" + "\n" + "$||v|| = " + f"\\sqrt{{{length_formula2}}}$" + "\n" + "$||v|| = " + f"\\sqrt{{{' + '.join(list(map(str, length_formula3)))}}}$" + "\n" + "$||v|| = " + f"\\sqrt{{{sum(length_formula3)}}}"
        else:
            latex_formula = "||v|| = \\sqrt{v \\cdot v}$" + "\n" + "$||v|| = " + f"\\sqrt{{{length_formula1}}}$" + "\n" + "$||v|| = " + f"\\sqrt{{{length_formula2}}}$" + "\n" + "$||v|| = " + f"\\sqrt{{{' + '.join(list(map(str, length_formula3)))}}}$" + "\n" + "$||v|| = " + f"\\sqrt{{{sum(length_formula3)}}}$" "\n" + "$||v|| = " + f"{int(sqrt(sum(length_formula3)))}"

    # untuk perhitungan angle
    elif name == "angle":
        dot_formula1 = " + ".join([f"(v_{x} \\times w_{y})" for x,y in zip([i for i in range(1, len(vector1) + 1)], [i for i in range(1, len(vector1) + 1)])])
        dot_formula2 = " + ".join([f"({x} \\times {y})" for x,y in zip(vector1, vector2)])
        dot_formula3 = " + ".join([f"{int(x) * int(y)}" for x,y in zip(vector1, vector2)])
        dot_result = vc.dot(list(map(int, vector1)), list(map(int, vector2)))

        length_formula_v1 = " + ".join(f"{{v_{{{x}}}}}^2" for x in [i for i in range(1, len(vector1) + 1)])
        length_formula_w1 = " + ".join(f"{{w_{{{x}}}}}^2" for x in [i for i in range(1, len(vector1) + 1)])
        length_formula_v2 = " + ".join(f"{{{i}}}^2" for i in vector1)
        length_formula_w2 = " + ".join(f"{{{i}}}^2" for i in vector2)
        length_formula_v3 = [pow(int(i), 2) for i in vector1]
        length_formula_w3 = [pow(int(i), 2) for i in vector2]
        length_result = vc.length(list(map(int, vector1)))



        angle_formula1 = "\\theta = \\arccos(\\frac{\\vec{v} \\cdot \\vec{w}}{||\\vec{v}|| \\times ||\\vec{w}||})"
        angle_formula2 = f"\\theta = \\arccos(\\frac{{{dot_formula1}}}{{\\sqrt{{{length_formula_v1}}} \\times \\sqrt{{{length_formula_w1}}}}})"
        angle_formula3 = f"\\theta = \\arccos(\\frac{{{dot_formula2}}}{{\\sqrt{{{length_formula_v2}}} \\times \\sqrt{{{length_formula_w2}}}}})"
        angle_formula4 = f"\\theta = \\arccos(\\frac{{{dot_formula3}}}{{\\sqrt{{{' + '.join(list(map(str, length_formula_v3)))}}} \\times \\sqrt{{{' + '.join(list(map(str, length_formula_w3)))}}}}})"
        angle_formula5 = f"\\theta = \\arccos(\\frac{{{dot_result}}}{{\\sqrt{{{sum(length_formula_v3)}}} \\times \\sqrt{{{sum(length_formula_w3)}}}}})"
        angle_formula6 = f"\\theta = \\arccos(\\frac{{{dot_result}}}{{\\sqrt{{{sum(length_formula_v3) * sum(length_formula_w3)}}}}})"
        angle_formula7 = f"\\theta = \\arccos(\\frac{{{dot_result}}}{{{sqrt(sum(length_formula_v3) * sum(length_formula_w3))}}})"
        angle_formula8 = f"\\theta = \\arccos({dot_result / sqrt(sum(length_formula_v3) * sum(length_formula_w3))})"
        angle_result = f"\\theta = {vc.angle(list(map(int, vector1)), list(map(int, vector2)))}°"

        latex_formula = angle_formula1 + "$\n$" + angle_formula2 + "$\n$" + angle_formula3 + "$\n$" + angle_formula4 + "$\n$" + angle_formula5 + "$\n$" + angle_formula6 + "$\n$" + angle_formula7 + "$\n$" + angle_formula8 + "$\n$" + angle_result

    png_path = latex_to_png(latex_formula)

    png_path = crop.crop_png(png_path, f"run/assets/{name}.png")

    return png_path
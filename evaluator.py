import json
import argparse

class ConfinedSpaceEvaluator:
    """
    Evaluador de riesgos para espacios confinados basado en la Resolución 0491 de 2020 (Colombia).
    """
    def __init__(self, o2_percentage, h2s_ppm=0.0, co_ppm=0.0, lel_percentage=0.0, access_restricted=True):
        self.o2 = o2_percentage
        self.h2s = h2s_ppm
        self.co = co_ppm
        self.lel = lel_percentage
        self.access_restricted = access_restricted

    def evaluate_atmosphere(self):
        warnings = []
        is_grade_a = False
        is_grade_b = False

        # Evaluación de Oxígeno (Res. 0491 Art. 6: Rango seguro 19.5% - 23.5%)
        if self.o2 < 19.5:
            warnings.append("Atmósfera Deficiente en Oxígeno (<19.5%). Riesgo Inminente de Asfixia.")
            is_grade_a = True
        elif self.o2 > 23.5:
            warnings.append("Atmósfera Enriquecida en Oxígeno (>23.5%). Alto riesgo de combustión.")
            is_grade_a = True

        # Evaluación de Gases Tóxicos (H2S TLV-TWA 1 ppm / CO TLV-TWA 25 ppm)
        if self.h2s >= 10.0 or self.co >= 25.0:
            warnings.append(f"Presencia de gases tóxicos por encima del límite permitido (H2S: {self.h2s}ppm, CO: {self.co}ppm).")
            is_grade_a = True
        elif self.h2s > 1.0 or self.co > 5.0:
            warnings.append("Presencia traza de gases tóxicos. Requiere monitoreo continuo.")
            is_grade_b = True

        # Evaluación de Explosividad / Inflamabilidad (% LEL)
        if self.lel >= 10.0:
            warnings.append(f"Atmósfera Inflamable/Explosiva (LEL: {self.lel}% >= 10%). Prohibido ingreso sin inertización.")
            is_grade_a = True
        elif self.lel > 0.0:
            warnings.append(f"Presencia de gases combustibles ({self.lel}% LEL).")
            is_grade_b = True

        # Clasificación por Grado de Peligro (Res 0491 Cap. II)
        if is_grade_a:
            grade = "Grado A (Inminentemente Peligroso para la Vida o Salud - IDLH)"
            risk_level = "ALTO / CRÍTICO"
        elif is_grade_b:
            grade = "Grado B (Peligro Potencial no Inminente)"
            risk_level = "MEDIO"
        else:
            grade = "Grado C (Atmósfera Aceptable / Bajo Riesgo)"
            risk_level = "BAJO"

        # Tipo de espacio (Tipo 1: Abierto por arriba / Tipo 2: Cerrado con accesos reducidos)
        space_type = "Tipo 1 (Abierto superior)" if not self.access_restricted else "Tipo 2 (Cerrado/Restringido)"

        return {
            "normativa": "Resolucion 0491 de 2020 (Colombia)",
            "grado_clasificacion": grade,
            "tipo_espacio": space_type,
            "nivel_riesgo": risk_level,
            "permiso_ingreso_requerido": True,  # Siempre requerido por ley en Colombia
            "monitoreo_continuo": is_grade_a or is_grade_b,
            "ventilar_antes_de_ingresar": len(warnings) > 0,
            "advertencias_seguridad": warnings
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluador de Espacios Confinados según Res 0491/2020 Colombia")
    parser.add_argument("--o2", type=float, default=20.9, help="Porcentaje de Oxígeno (% O2)")
    parser.add_argument("--h2s", type=float, default=0.0, help="Gas Sulfhídrico (PPM H2S)")
    parser.add_argument("--co", type=float, default=0.0, help="Monóxido de Carbono (PPM CO)")
    parser.add_argument("--lel", type=float, default=0.0, help="Límite Inferior de Explosividad (% LEL)")
    
    args = parser.parse_args()
    evaluator = ConfinedSpaceEvaluator(args.o2, args.h2s, args.co, args.lel)
    print(json.dumps(evaluator.evaluate_atmosphere(), indent=2, ensure_ascii=False))

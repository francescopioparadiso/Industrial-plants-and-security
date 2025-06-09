import os

def latex_update(updates: dict):
    document_path = '/Users/francescopioparadiso/Library/Mobile Documents/com~apple~CloudDocs/PARADISO/01. Francesco/01. Education/02. University/BSc Politecnico di Torino/3 Year/02. Impianti industriali e sicurezza sul lavoro/Progetto/Report/report.tex'
    updated_path = '/Users/francescopioparadiso/Library/Mobile Documents/com~apple~CloudDocs/PARADISO/01. Francesco/01. Education/02. University/BSc Politecnico di Torino/3 Year/02. Impianti industriali e sicurezza sul lavoro/Progetto/Report/LaTeX/updated_report.tex'

    # Delete old file explicitly if it exists
    if os.path.exists(updated_path):
        os.remove(updated_path)

    # Read original LaTeX
    with open(document_path, 'r') as file:
        latex_content = file.read()

    # Apply substitutions
    for reference, value in updates.items():
        latex_content = latex_content.replace('{{' + reference + '}}', str(value))

    # Write new content
    with open(updated_path, 'w') as file:
        file.write(latex_content)

if __name__ == "__main__":
    updates = {}

    # First page ---------------------------------------------------------------------------------
    # Definizione dettagli studenti con team
    students = [
        {"name": "Palandri Daniele", "id": 307084, "team": "A"},
        {"name": "Palmisano Alessio", "id": 310880, "team": "A"},
        {"name": "Paradiso Francesco Pio", "id": 310834, "team": "A"},
        {"name": "Pellicanò Clarissa", "id": 297953, "team": "A"},
        {"name": "Regis Milano Carlo", "id": 310989, "team": "A"},
        {"name": "Santacroce Gabriele", "id": 307587, "team": "A"},
        {"name": "Scarcina Gabriele", "id": 312112, "team": "A"},
        {"name": "Zocco Stefano", "id": 299769, "team": "A"},
        {"name": "Ore Flores Akil", "id": 313890, "team": "B"},
        {"name": "Palla Federico", "id": 314742, "team": "B"},
        {"name": "Ruggirello Gioacchino", "id": 310831, "team": "B"},
        {"name": "Sinatra Giuseppe", "id": 312211, "team": "B"},
        {"name": "Tigri Andrea", "id": 311364, "team": "B"},
        {"name": "Turzo Costantino", "id": 272712, "team": "B"},
        {"name": "Zanco Nicholas", "id": 297395, "team": "B"},
        {"name": "Zannotti Nicola", "id": 328111, "team": "B"},
    ]

    # Ordina prima per team, poi per nome
    students_sorted = sorted(students, key=lambda x: (x["team"], x["name"]))

    # Divide in due colonne: primi 8 (team A), ultimi 8 (team B)
    team_a = [s for s in students_sorted if s["team"] == "A"]
    team_b = [s for s in students_sorted if s["team"] == "B"]

    # Inserisce i nomi e ID nelle variabili updates
    for i, student in enumerate(team_a):
        updates[f"studentName{i}"] = student["name"]
        updates[f"studentId{i}"] = student["id"]
    for i, student in enumerate(team_b):
        updates[f"studentName{i+len(team_a)}"] = student["name"]
        updates[f"studentId{i+len(team_a)}"] = student["id"]

    # Attachment names ----------------------------------------------------------------
    updates["excelA1B"] = r"\attachfile[description={01. Plancia A1-B.xlsx}]{attachments/01. Plancia A1-B.xlsx}{\texttt{01. Plancia A1-B.xlsx}}"
    updates["excelA2D"] = r"\attachfile[description={02. Plancia A2-D.xlsx}]{attachments/02. Plancia A2-D.xlsx}{\texttt{02. Plancia A2-D.xlsx}}"
    updates["matriceWBSOBS"] = r"\attachfile[description={03. Matrice WBS-OBS.xlsx}]{attachments/03. Matrice WBS-OBS.xlsx}{\texttt{03. Matrice WBS-OBS.xlsx}}"
    updates["excelCompleto"] = r"\attachfile[description={04. Excel completo.xlsx}]{attachments/04. Excel completo.xlsx}{\texttt{04. Excel completo.xlsx}}"
    updates["gantt"] = r"\attachfile[description={05. Gantt.xlsx}]{attachments/05. Gantt.xlsx}{\texttt{05. Gantt.xlsx}}"
    updates["ariaCompressaAssemblaggio"] = r"\attachfile[description={06. Aria compressa assemblaggio.xlsx}]{attachments/06. Aria compressa assemblaggio.xlsx}{\texttt{06. Aria compressa assemblaggio.xlsx}}"
    updates["distintaBase"] = r"\attachfile[description={07. Distinta base.pdf}]{attachments/07. Distinta base.pdf}{\texttt{07. Distinta base.pdf}}"
    updates["processoProduttivo"] = r"\attachfile[description={08. Processo produttivo.pdf}]{attachments/08. Processo produttivo.pdf}{\texttt{08. Processo produttivo.pdf}}"
    updates["elevatoreBTSTAXIO"] = r"\attachfile[description={09. Elevatore BT STAXIO.pdf}]{attachments/09. Elevatore BT STAXIO.pdf}{\texttt{09. Elevatore BT STAXIO.pdf}}"
    updates["transpalletBTLIFTER"] = r"\attachfile[description={10. Transpallet BT LIFTER.pdf}]{attachments/10. Transpallet BT LIFTER.pdf}{\texttt{10. Transpallet BT LIFTER.pdf}}"
    updates["layoutPostazioneSaldatura"] = r"\attachfile[description={11. Studio postazione saldatura.pdf}]{attachments/11. Studio postazione saldatura.pdf}{\texttt{11. Studio postazione saldatura.pdf}}"
    updates["layoutPostazioneAssemblaggio"] = r"\attachfile[description={12. Studio postazione assemblaggio.pdf}]{attachments/12. Studio postazione assemblaggio.pdf}{\texttt{12. Studio postazione assemblaggio.pdf}}"
    updates["areaRicezione"] = r"\attachfile[description={13. Area ricezione.pdf}]{attachments/13. Area ricezione.pdf}{\texttt{13. Area ricezione.pdf}}"
    updates["areaPicking"] = r"\attachfile[description={14. Area picking.pdf}]{attachments/14. Area picking.pdf}{\texttt{14. Area picking.pdf}}"
    updates["areaInterna"] = r"\attachfile[description={15. Area interna.pdf}]{attachments/15. Area interna.pdf}{\texttt{15. Area interna.pdf}}"
    updates["areaRicarica"] = r"\attachfile[description={16. Area ricarica.pdf}]{attachments/16. Area ricarica.pdf}{\texttt{16. Area ricarica.pdf}}"
    updates["areaParcheggi"] = r"\attachfile[description={17. Area parcheggi.pdf}]{attachments/17. Area parcheggi.pdf}{\texttt{17. Area parcheggi.pdf}}"
    updates["collocazioneStabilimento"] = r"\attachfile[description={18. Collocazione stabilimento.pdf}]{attachments/18. Collocazione stabilimento.pdf}{\texttt{18. Collocazione stabilimento.pdf}}"
    updates["spaghettiChartA1"] = r"\attachfile[description={19. Spaghetti Chart A1.pdf}]{attachments/19. Spaghetti Chart A1.pdf}{\texttt{19. Spaghetti Chart A1.pdf}}"
    updates["spaghettiChartB"] = r"\attachfile[description={20. Spaghetti Chart B.pdf}]{attachments/20. Spaghetti Chart B.pdf}{\texttt{20. Spaghetti Chart B.pdf}}"
    updates["spaghettiChartA2"] = r"\attachfile[description={21. Spaghetti Chart A2.pdf}]{attachments/21. Spaghetti Chart A2.pdf}{\texttt{21. Spaghetti Chart A2.pdf}}"
    updates["spaghettiChartD"] = r"\attachfile[description={22. Spaghetti Chart D.pdf}]{attachments/22. Spaghetti Chart D.pdf}{\texttt{22. Spaghetti Chart D.pdf}}"
    updates["planimetriaInternoEsterno"] = r"\attachfile[description={23. Planimetria interno ed esterno.pdf}]{attachments/23. Planimetria interno ed esterno.pdf}{\texttt{23. Planimetria interno ed esterno.pdf}}"
    updates["planimetriaInternaConPiani"] = r"\attachfile[description={24. Planimetria interna con piani.pdf}]{attachments/24. Planimetria interna con piani.pdf}{\texttt{24. Planimetria interna con piani.pdf}}"

    latex_update(updates)

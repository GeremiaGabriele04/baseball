import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._choiceTeam = None

    def handleCreaGrafo(self, e):
        pass

    def handleDettagli(self, e):
        pass

    def handlePercorso(self, e):
        pass

    def fillDDYears(self):
        years = self._model.getAllYears()

        #yearsDD = []
        #for y in years:
        #    yearsDD.append(ft.dropdown.Option(y))

        yearsDD = list(map(lambda x: ft.dropdown.Option(x), years)) #METTERE list(map(....))
        self._view._ddAnno.options = yearsDD
        self._view.update_page()

    def handleYearSelection(self):
        #attivato quando si seleziona un anno dal DD
        #deve selezionare tutti i team  che hanno giocato nell'anno e stamparli nel textFIeld
        #e anche riempire il DD sotto
        if self._view._ddAnno.value is None:
            self._view._txtOutSquadre.controls.clear()
            self._view._txtOutSquadre.controls.append(ft.Text("Selezionare un anno dal menu"))

        teams = self._model.getTeamsOfYear(self._view._ddAnno.value)

        self._view._txtOutSquadre.controls.clear()
        self._view._txtOutSquadre.controls.append(ft.Text("Sono iscritte le seguenti squadre:"))
        for t in teams:
            self._view._txtOutSquadre.controls.append(ft.Text(t))
            self._view._ddSquadra.options.append(
                ft.dropdown.Option(data = t,
                                   text = t.name,
                                   on_click = self.readDDTeams)
            )
        self._view.update_page()

    def readDDTeams(self, e):
        self._choiceTeam = e.control.data
        return self._choiceTeam

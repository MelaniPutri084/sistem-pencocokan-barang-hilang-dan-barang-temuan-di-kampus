
from models.laporan_model import LaporanModel
from views.laporan_view import LaporanView
from controllers.laporan_controller import LaporanController


def main():
    model = LaporanModel()
    view = LaporanView()

    LaporanController(model, view)

    view.mainloop()


if __name__ == "__main__":
    main()
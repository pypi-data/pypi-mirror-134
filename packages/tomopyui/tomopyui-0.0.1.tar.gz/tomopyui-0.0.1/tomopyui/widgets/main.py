import tomopyui.widgets.meta as meta
from ipywidgets import *
from tomopyui.widgets._shared.helpers import import_module_set_env

# checks if cupy is installed. if not, disable cuda and certain gui aspects
# TODO: can put this somewhere else (in meta?)
cuda_import_dict = {"cupy": "cuda_enabled"}
import_module_set_env(cuda_import_dict)

# checks how many cpus available for compute on CPU
# TODO: can later add a bounded textbox for amount of CPUs user wants to use
# for reconstruction. right now defaults to all cores being used.
import multiprocessing
os.environ["num_cpu_cores"] = str(multiprocessing.cpu_count())

def create_dashboard():
    """
    This is the function to open the app in a jupyter notebook. In jupyter,
    run the following commands:

    .. code-block:: python

        %matplotlib ipympl
        import tomopyui.widgets.main as main

        dashboard, file_import, center, prep, align, recon = main.create_dashboard()
        dashboard

    """

    file_import = meta.Import()
    center_tab_obj = meta.Center(file_import)
    prep_tab_obj = meta.Prep(file_import)
    recon_tab_obj = meta.Recon(file_import, center_tab_obj)
    align_tab_obj = meta.Align(file_import, center_tab_obj)
    for checkbox in align_tab_obj.astra_cuda_methods_checkboxes + recon_tab_obj.astra_cuda_methods_checkboxes:
        if os.environ["cuda_enabled"] == "True":
            checkbox.disabled = False
        else:
            checkbox.disabled = True
    dashboard_tabs = [
        file_import.tab,
        center_tab_obj.center_tab,
        align_tab_obj.tab,
        recon_tab_obj.tab,
        file_import.log_handler.out,
    ]

    dashboard_titles = ["Import", "Center", "Align", "Reconstruct", "Log"]
    dashboard = Tab(titles=dashboard_titles)
    dashboard.children = dashboard_tabs
    return (
        dashboard,
        file_import,
        center_tab_obj,
        prep_tab_obj,
        align_tab_obj,
        recon_tab_obj,
    )

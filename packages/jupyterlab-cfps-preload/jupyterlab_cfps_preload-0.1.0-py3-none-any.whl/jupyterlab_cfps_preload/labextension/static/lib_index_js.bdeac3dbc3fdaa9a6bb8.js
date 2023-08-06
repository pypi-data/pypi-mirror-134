(self["webpackChunkjupyterlab_cfps_preload"] = self["webpackChunkjupyterlab_cfps_preload"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((module) => {

module.exports = [
    {
        id: 'jupyterlab_cfps_preload',
        autoStart: true,
        activate: function (app) {
            console.log(
                'JupyterLab extension jupyterlab_cfps_preload is activated!'
            );
            new Promise(function (resolve, reject) {
                var script = document.createElement("script");
                script.onload = resolve;
                script.onerror = reject;
                script.src = "https://assets.pyecharts.org/assets/echarts.min.js";
                document.head.appendChild(script);
            }).then(() => {
                console.log("echarts.min.js loaded");
            });
            console.log(app.commands);
        }
    }
];


/***/ })

}]);
//# sourceMappingURL=lib_index_js.bdeac3dbc3fdaa9a6bb8.js.map
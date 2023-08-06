(self["webpackChunkjupyterlab_cfps_preload"] = self["webpackChunkjupyterlab_cfps_preload"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

loadEcharts = __webpack_require__(Object(function webpackMissingModule() { var e = new Error("Cannot find module 'load-echarts'"); e.code = 'MODULE_NOT_FOUND'; throw e; }()));

module.exports = [
    {
        id: 'jupyterlab_cfps_preload',
        autoStart: true,
        activate: function (app) {
            console.log(
                'JupyterLab extension jupyterlab_cfps_preload is activated!'
            );
            new Promise(async function (resolve, reject) {
                    let counter = 5;
                    while (counter-- > 0) {
                        if (await loadEcharts()) break;
                        else console.log("Retrying...");
                    }
                }
            ).then(() => {
            })

            console.log(app.commands);
        }
    }
];


/***/ })

}]);
//# sourceMappingURL=lib_index_js.8450d0c583b4ffc84237.js.map
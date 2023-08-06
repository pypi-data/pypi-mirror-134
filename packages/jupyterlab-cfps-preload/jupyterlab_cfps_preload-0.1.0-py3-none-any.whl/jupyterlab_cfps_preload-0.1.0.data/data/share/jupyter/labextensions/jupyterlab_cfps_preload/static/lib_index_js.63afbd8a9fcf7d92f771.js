(self["webpackChunkjupyterlab_cfps_preload"] = self["webpackChunkjupyterlab_cfps_preload"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

loadEcharts = __webpack_require__(/*! ./load-echarts.js */ "./lib/load-echarts.js");

module.exports = [
    {
        id: 'jupyterlab_cfps_preload',
        autoStart: true,
        activate: async function (app) {
            console.log(
                'JupyterLab extension jupyterlab_cfps_preload is activated!'
            );
            let counter = 5;
            while (counter-- > 0) {
                if (await loadEcharts()) {
                    return;
                } else console.log("Retrying...");
            }

            console.log(app.commands);
        }
    }
];


/***/ }),

/***/ "./lib/load-echarts.js":
/*!*****************************!*\
  !*** ./lib/load-echarts.js ***!
  \*****************************/
/***/ ((module) => {

async function loadEcharts() {
    return await new Promise(function (resolve, reject) {
        const script = document.createElement("script");
        script.onload = resolve;
        script.onerror = reject;
        script.src = "https://assets.pyecharts.org/assets/echarts.min.js";
        document.head.appendChild(script);
    }).then(() => {
        console.log("echarts.min.js loaded");
        return true;
    }).catch(() => {
        console.log("echarts.min.js failed to load");
        return false;
    });
}

module.exports = loadEcharts;

/***/ })

}]);
//# sourceMappingURL=lib_index_js.63afbd8a9fcf7d92f771.js.map
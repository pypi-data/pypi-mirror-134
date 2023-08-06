(self["webpackChunkjupyterlab_cfps_preload"] = self["webpackChunkjupyterlab_cfps_preload"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _load_echarts__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./load-echarts */ "./lib/load-echarts.js");
/* module decorator */ module = __webpack_require__.hmd(module);


module.exports = [
    {
        id: 'jupyterlab_cfps_preload',
        autoStart: true,
        activate: function (app) {
            console.log(
                'JupyterLab extension jupyterlab_cfps_preload is activated!'
            );
            let counter = 5;
            while (counter--) {
                if ((0,_load_echarts__WEBPACK_IMPORTED_MODULE_0__["default"])()) break;
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
/***/ (() => {

throw new Error("Module parse failed: Cannot use keyword 'await' outside an async function (2:17)\nYou may need an appropriate loader to handle this file type, currently no loaders are configured to process this file. See https://webpack.js.org/concepts#loaders\n| function loadEcharts() {\n>     let result = await new Promise(function (resolve, reject) {\n|         var script = document.createElement(\"script\");\n|         script.onload = resolve;");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.b3e76cc7be2dead16eac.js.map
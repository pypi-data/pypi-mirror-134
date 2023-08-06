"use strict";
(self["webpackChunkjupyterlab_cfps_preload"] = self["webpackChunkjupyterlab_cfps_preload"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

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
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
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

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (loadEcharts);

/***/ })

}]);
//# sourceMappingURL=lib_index_js.7ed2b272cf5b9100b3ab.js.map
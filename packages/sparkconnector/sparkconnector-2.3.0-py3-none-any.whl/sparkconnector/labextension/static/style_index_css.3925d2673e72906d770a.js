"use strict";
(self["webpackChunk_swan_cern_sparkconnector"] = self["webpackChunk_swan_cern_sparkconnector"] || []).push([["style_index_css"],{

/***/ "./node_modules/css-loader/dist/cjs.js!./style/index.css":
/*!***************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/index.css ***!
  \***************************************************************/
/***/ ((module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/cssWithMappingToString.js */ "./node_modules/css-loader/dist/runtime/cssWithMappingToString.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/getUrl.js */ "./node_modules/css-loader/dist/runtime/getUrl.js");
/* harmony import */ var _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _Apache_Spark_logo_png__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./Apache_Spark_logo.png */ "./style/Apache_Spark_logo.png");
// Imports




var ___CSS_LOADER_EXPORT___ = _node_modules_css_loader_dist_runtime_api_js__WEBPACK_IMPORTED_MODULE_1___default()((_node_modules_css_loader_dist_runtime_cssWithMappingToString_js__WEBPACK_IMPORTED_MODULE_0___default()));
var ___CSS_LOADER_URL_REPLACEMENT_0___ = _node_modules_css_loader_dist_runtime_getUrl_js__WEBPACK_IMPORTED_MODULE_2___default()(_Apache_Spark_logo_png__WEBPACK_IMPORTED_MODULE_3__["default"]);
// Module
___CSS_LOADER_EXPORT___.push([module.id, ".jp-SparkConnector {\n  display: flex;\n  flex-direction: column;\n  background: var(--jp-layout-color1);\n  color: var(--jp-ui-font-color1);\n  font-size: var(--jp-ui-font-size0);\n  height: 100%;\n  overflow: auto;\n}\n\n.jp-SparkConnector-scrollable {\n  overflow: auto;\n  display: flex;\n  flex-direction: column;\n  flex-grow: 1;\n}\n\n.jp-SparkConnector-details {\n  margin: 0px;\n  font-size: var(--jp-ui-font-size1);\n}\n\n.jp-SparkConnector-section-header {\n  flex: 0 0 auto;\n  font-weight: 600;\n  text-transform: uppercase;\n  letter-spacing: 1px;\n  padding: 8px;\n  font-size: var(--jp-ui-font-size0);\n  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);\n}\n\n.jp-SparkConnector-failed {\n  flex-grow: 1;\n}\n.jp-SparkConnector-failed .jp-SparkConnector-confDetailsContainer-sparkLogs {\n  margin: 8px;\n  transition: height 2s;\n}\n.jp-SparkConnector-panel {\n  display: flex;\n  flex-direction: row;\n  color: var(--jp-ui-font-color3);\n  height: 24px;\n  line-height: 24px;\n  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);\n}\n\n.jp-SparkConnector-panelLabel {\n  font-size: var(--jp-ui-font-size0);\n  font-weight: 600;\n  flex: 1 1 auto;\n  margin-right: 4px;\n  padding-left: 8px;\n  text-overflow: ellipsis;\n  overflow: hidden;\n  white-space: nowrap;\n  border-radius: 2px;\n  text-transform: uppercase;\n  letter-spacing: 1px;\n}\n\n.jp-SparkConnector-loading {\n  display: flex;\n  flex-direction: column;\n  height: 300px;\n  width: 100%;\n  align-items: center;\n  justify-content: center;\n  margin: 20px 0;\n  flex: 1 0;\n}\n\n.jp-SparkConnector-confDetailsContainer-sparkLogs {\n  padding: 4px 4px 4px 4px;\n  border-bottom: var(--jp-border-width) solid transparent;\n  border-radius: var(--jp-border-radius);\n}\n\n.jp-SparkConnector-confDetailsContainer-sparkLogs pre {\n  font-size: var(--jp-ui-font-size0);\n}\n\n.jp-SparkConnector-confDetailsContainer-sparkLogs.info {\n  color: var(--jp-ui-font-color1);\n  background-color: var(--jp-layout-color2);\n  border-color: var(--md-grey-300);\n  overflow: auto;\n  word-wrap: break-word;\n  flex-grow: 1;\n}\n\n.jp-SparkConnector-logo {\n  background-image: url(" + ___CSS_LOADER_URL_REPLACEMENT_0___ + ");\n  background-size: contain;\n  background-repeat: no-repeat;\n  background-position: center center;\n  height: 40px;\n  width: 100%;\n}\n.jp-SparkConnector-connectionDetailsContainer {\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  padding: 4px;\n}\n.jp-SparkConnector-notattached {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100%;\n  opacity: 0.4;\n  padding: 8px;\n}\n.jp-SparkConnector-connectionDetailsContainerInfo {\n  opacity: 0.4;\n}\n\n.jp-SparkConnector-input-sparkopts {\n  display: flex;\n  flex-direction: column;\n  padding: 4px;\n}\n.jp-SparkConnector-button-main {\n  margin: 8px !important;\n}\n.jp-SparkConnector-input-sparkopts > * {\n  margin-bottom: 8px !important;\n}\n.jp-SparkConnector-logs {\n  flex-grow: 1;\n  display: flex;\n  flex-direction: column;\n  min-height: 0;\n}\n\n.jp-SparkConnector-auth {\n  flex-grow: 1;\n  padding: 8px;\n}\n.jp-SparkConnector-auth > * {\n  margin-bottom: 8px;\n}\n.jp-SparkConnector-error * {\n  word-break: break-all;\n}\n.jp-SparkConnector-selected-config {\n  word-break: break-all;\n}\n\n.jp-SparkConnector-logrefresh {\n  height: 10px;\n  width: 10px;\n  margin: 0;\n  padding: 0;\n  float: right;\n}\n", "",{"version":3,"sources":["webpack://./style/index.css"],"names":[],"mappings":"AAAA;EACE,aAAa;EACb,sBAAsB;EACtB,mCAAmC;EACnC,+BAA+B;EAC/B,kCAAkC;EAClC,YAAY;EACZ,cAAc;AAChB;;AAEA;EACE,cAAc;EACd,aAAa;EACb,sBAAsB;EACtB,YAAY;AACd;;AAEA;EACE,WAAW;EACX,kCAAkC;AACpC;;AAEA;EACE,cAAc;EACd,gBAAgB;EAChB,yBAAyB;EACzB,mBAAmB;EACnB,YAAY;EACZ,kCAAkC;EAClC,mEAAmE;AACrE;;AAEA;EACE,YAAY;AACd;AACA;EACE,WAAW;EACX,qBAAqB;AACvB;AACA;EACE,aAAa;EACb,mBAAmB;EACnB,+BAA+B;EAC/B,YAAY;EACZ,iBAAiB;EACjB,mEAAmE;AACrE;;AAEA;EACE,kCAAkC;EAClC,gBAAgB;EAChB,cAAc;EACd,iBAAiB;EACjB,iBAAiB;EACjB,uBAAuB;EACvB,gBAAgB;EAChB,mBAAmB;EACnB,kBAAkB;EAClB,yBAAyB;EACzB,mBAAmB;AACrB;;AAEA;EACE,aAAa;EACb,sBAAsB;EACtB,aAAa;EACb,WAAW;EACX,mBAAmB;EACnB,uBAAuB;EACvB,cAAc;EACd,SAAS;AACX;;AAEA;EACE,wBAAwB;EACxB,uDAAuD;EACvD,sCAAsC;AACxC;;AAEA;EACE,kCAAkC;AACpC;;AAEA;EACE,+BAA+B;EAC/B,yCAAyC;EACzC,gCAAgC;EAChC,cAAc;EACd,qBAAqB;EACrB,YAAY;AACd;;AAEA;EACE,yDAA8C;EAC9C,wBAAwB;EACxB,4BAA4B;EAC5B,kCAAkC;EAClC,YAAY;EACZ,WAAW;AACb;AACA;EACE,aAAa;EACb,sBAAsB;EACtB,mBAAmB;EACnB,YAAY;AACd;AACA;EACE,aAAa;EACb,uBAAuB;EACvB,mBAAmB;EACnB,YAAY;EACZ,YAAY;EACZ,YAAY;AACd;AACA;EACE,YAAY;AACd;;AAEA;EACE,aAAa;EACb,sBAAsB;EACtB,YAAY;AACd;AACA;EACE,sBAAsB;AACxB;AACA;EACE,6BAA6B;AAC/B;AACA;EACE,YAAY;EACZ,aAAa;EACb,sBAAsB;EACtB,aAAa;AACf;;AAEA;EACE,YAAY;EACZ,YAAY;AACd;AACA;EACE,kBAAkB;AACpB;AACA;EACE,qBAAqB;AACvB;AACA;EACE,qBAAqB;AACvB;;AAEA;EACE,YAAY;EACZ,WAAW;EACX,SAAS;EACT,UAAU;EACV,YAAY;AACd","sourcesContent":[".jp-SparkConnector {\n  display: flex;\n  flex-direction: column;\n  background: var(--jp-layout-color1);\n  color: var(--jp-ui-font-color1);\n  font-size: var(--jp-ui-font-size0);\n  height: 100%;\n  overflow: auto;\n}\n\n.jp-SparkConnector-scrollable {\n  overflow: auto;\n  display: flex;\n  flex-direction: column;\n  flex-grow: 1;\n}\n\n.jp-SparkConnector-details {\n  margin: 0px;\n  font-size: var(--jp-ui-font-size1);\n}\n\n.jp-SparkConnector-section-header {\n  flex: 0 0 auto;\n  font-weight: 600;\n  text-transform: uppercase;\n  letter-spacing: 1px;\n  padding: 8px;\n  font-size: var(--jp-ui-font-size0);\n  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);\n}\n\n.jp-SparkConnector-failed {\n  flex-grow: 1;\n}\n.jp-SparkConnector-failed .jp-SparkConnector-confDetailsContainer-sparkLogs {\n  margin: 8px;\n  transition: height 2s;\n}\n.jp-SparkConnector-panel {\n  display: flex;\n  flex-direction: row;\n  color: var(--jp-ui-font-color3);\n  height: 24px;\n  line-height: 24px;\n  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);\n}\n\n.jp-SparkConnector-panelLabel {\n  font-size: var(--jp-ui-font-size0);\n  font-weight: 600;\n  flex: 1 1 auto;\n  margin-right: 4px;\n  padding-left: 8px;\n  text-overflow: ellipsis;\n  overflow: hidden;\n  white-space: nowrap;\n  border-radius: 2px;\n  text-transform: uppercase;\n  letter-spacing: 1px;\n}\n\n.jp-SparkConnector-loading {\n  display: flex;\n  flex-direction: column;\n  height: 300px;\n  width: 100%;\n  align-items: center;\n  justify-content: center;\n  margin: 20px 0;\n  flex: 1 0;\n}\n\n.jp-SparkConnector-confDetailsContainer-sparkLogs {\n  padding: 4px 4px 4px 4px;\n  border-bottom: var(--jp-border-width) solid transparent;\n  border-radius: var(--jp-border-radius);\n}\n\n.jp-SparkConnector-confDetailsContainer-sparkLogs pre {\n  font-size: var(--jp-ui-font-size0);\n}\n\n.jp-SparkConnector-confDetailsContainer-sparkLogs.info {\n  color: var(--jp-ui-font-color1);\n  background-color: var(--jp-layout-color2);\n  border-color: var(--md-grey-300);\n  overflow: auto;\n  word-wrap: break-word;\n  flex-grow: 1;\n}\n\n.jp-SparkConnector-logo {\n  background-image: url('Apache_Spark_logo.png');\n  background-size: contain;\n  background-repeat: no-repeat;\n  background-position: center center;\n  height: 40px;\n  width: 100%;\n}\n.jp-SparkConnector-connectionDetailsContainer {\n  display: flex;\n  flex-direction: column;\n  align-items: center;\n  padding: 4px;\n}\n.jp-SparkConnector-notattached {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n  height: 100%;\n  opacity: 0.4;\n  padding: 8px;\n}\n.jp-SparkConnector-connectionDetailsContainerInfo {\n  opacity: 0.4;\n}\n\n.jp-SparkConnector-input-sparkopts {\n  display: flex;\n  flex-direction: column;\n  padding: 4px;\n}\n.jp-SparkConnector-button-main {\n  margin: 8px !important;\n}\n.jp-SparkConnector-input-sparkopts > * {\n  margin-bottom: 8px !important;\n}\n.jp-SparkConnector-logs {\n  flex-grow: 1;\n  display: flex;\n  flex-direction: column;\n  min-height: 0;\n}\n\n.jp-SparkConnector-auth {\n  flex-grow: 1;\n  padding: 8px;\n}\n.jp-SparkConnector-auth > * {\n  margin-bottom: 8px;\n}\n.jp-SparkConnector-error * {\n  word-break: break-all;\n}\n.jp-SparkConnector-selected-config {\n  word-break: break-all;\n}\n\n.jp-SparkConnector-logrefresh {\n  height: 10px;\n  width: 10px;\n  margin: 0;\n  padding: 0;\n  float: right;\n}\n"],"sourceRoot":""}]);
// Exports
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (___CSS_LOADER_EXPORT___);


/***/ }),

/***/ "./style/Apache_Spark_logo.png":
/*!*************************************!*\
  !*** ./style/Apache_Spark_logo.png ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (__webpack_require__.p + "c7afd77757c0cf13826d9ac63d0e4ef10ab3f59b4840dd42f1666ffacf7d5882.png");

/***/ }),

/***/ "./style/index.css":
/*!*************************!*\
  !*** ./style/index.css ***!
  \*************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
/* harmony import */ var _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./index.css */ "./node_modules/css-loader/dist/cjs.js!./style/index.css");

            

var options = {};

options.insert = "head";
options.singleton = false;

var update = _node_modules_style_loader_dist_runtime_injectStylesIntoStyleTag_js__WEBPACK_IMPORTED_MODULE_0___default()(_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"], options);



/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (_node_modules_css_loader_dist_cjs_js_index_css__WEBPACK_IMPORTED_MODULE_1__["default"].locals || {});

/***/ })

}]);
//# sourceMappingURL=style_index_css.3925d2673e72906d770a.js.map
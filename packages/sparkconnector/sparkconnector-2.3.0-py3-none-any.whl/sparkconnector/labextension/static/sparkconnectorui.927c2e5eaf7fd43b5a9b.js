"use strict";
(self["webpackChunk_swan_cern_sparkconnector"] = self["webpackChunk_swan_cern_sparkconnector"] || []).push([["sparkconnectorui"],{

/***/ "./lib/components/authenticate.js":
/*!****************************************!*\
  !*** ./lib/components/authenticate.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Authenticate": () => (/* binding */ Authenticate)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _material_ui_core_Button__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/core/Button */ "./node_modules/@material-ui/core/esm/Button/Button.js");
/* harmony import */ var _material_ui_icons_VpnKey__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @material-ui/icons/VpnKey */ "./node_modules/@material-ui/icons/VpnKey.js");
/* harmony import */ var _material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/core/TextField */ "./node_modules/@material-ui/core/esm/TextField/TextField.js");
/* harmony import */ var _material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/lab/Alert */ "./node_modules/@material-ui/lab/esm/Alert/Alert.js");
/* harmony import */ var _material_ui_lab_AlertTitle__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/lab/AlertTitle */ "./node_modules/@material-ui/lab/esm/AlertTitle/AlertTitle.js");
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../store */ "./lib/store.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./common/layout */ "./lib/components/common/layout.js");









const Authenticate = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    const [password, setPassword] = react__WEBPACK_IMPORTED_MODULE_0___default().useState('');
    let displayError = '';
    if (_store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.authError) {
        displayError = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_4__["default"], { severity: "error" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_lab_AlertTitle__WEBPACK_IMPORTED_MODULE_5__["default"], null, "Error"),
            _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.authError));
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Section, { title: "Authentication", className: "jp-SparkConnector-auth" },
            displayError,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_4__["default"], { severity: "info" }, "Before connecting to the cluster, we need to obtain a Kerberos ticket. Please enter your account password."),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_6__["default"], { id: "standard-password-input", size: "small", variant: "outlined", label: "Password", type: "password", autoComplete: "current-password", value: password, fullWidth: true, onChange: (event) => {
                    setPassword(event.target.value);
                } })),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Button__WEBPACK_IMPORTED_MODULE_7__["default"], { color: "primary", variant: "contained", disabled: !password, onClick: () => {
                _store__WEBPACK_IMPORTED_MODULE_2__.store.onClickAuthenticate(password);
            }, startIcon: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_VpnKey__WEBPACK_IMPORTED_MODULE_8__["default"], null), className: "jp-SparkConnector-button-main" }, "Authenticate")));
});


/***/ }),

/***/ "./lib/components/common/layout.js":
/*!*****************************************!*\
  !*** ./lib/components/common/layout.js ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Layout": () => (/* binding */ Layout),
/* harmony export */   "Section": () => (/* binding */ Section)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../store */ "./lib/store.js");
/* harmony import */ var _spark_version__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./spark-version */ "./lib/components/common/spark-version.js");




const Title = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    var _a, _b;
    let notebookName = '';
    if ((_a = _store__WEBPACK_IMPORTED_MODULE_2__.store === null || _store__WEBPACK_IMPORTED_MODULE_2__.store === void 0 ? void 0 : _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook) === null || _a === void 0 ? void 0 : _a.title) {
        notebookName = '| ' + ((_b = _store__WEBPACK_IMPORTED_MODULE_2__.store === null || _store__WEBPACK_IMPORTED_MODULE_2__.store === void 0 ? void 0 : _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook) === null || _b === void 0 ? void 0 : _b.title);
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-panel" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { className: "jp-SparkConnector-panelLabel" },
            "Apache Spark ",
            notebookName)));
});
const Layout = (props) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Title, null),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_spark_version__WEBPACK_IMPORTED_MODULE_3__.SparkConnectionDetails, null),
        props.children));
};
const Section = (props) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("header", { className: "jp-SparkConnector-section-header" },
            props.title,
            props.extraActions),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: 'jp-SparkConnector-details ' + props.className || 0 }, props.children)));
};


/***/ }),

/***/ "./lib/components/common/loglist.js":
/*!******************************************!*\
  !*** ./lib/components/common/loglist.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LogList": () => (/* binding */ LogList)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../store */ "./lib/store.js");



/*
  Display a list of log output in monospace font.
*/
const LogList = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    const logEndDivRef = react__WEBPACK_IMPORTED_MODULE_0___default().useRef(null);
    react__WEBPACK_IMPORTED_MODULE_0___default().useEffect(() => {
        var _a;
        (_a = logEndDivRef.current) === null || _a === void 0 ? void 0 : _a.scrollIntoView({ behavior: 'smooth' });
    }, [_store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.logs]);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-confDetailsContainer-sparkLogs info" },
        _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.logs.map((log, idx) => {
            return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("pre", { key: idx }, log);
        }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { ref: logEndDivRef })));
});


/***/ }),

/***/ "./lib/components/common/spark-version.js":
/*!************************************************!*\
  !*** ./lib/components/common/spark-version.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SparkConnectionDetails": () => (/* binding */ SparkConnectionDetails)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../store */ "./lib/store.js");



const SparkConnectionDetails = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    var _a, _b;
    let details = '';
    if (((_a = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook) === null || _a === void 0 ? void 0 : _a.clusterName) &&
        ((_b = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook) === null || _b === void 0 ? void 0 : _b.sparkVersion)) {
        details = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-connectionDetailsContainerInfo" },
            "Cluster ",
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("b", null, _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.clusterName),
            " | Version",
            ' ',
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("b", null, _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.sparkVersion)));
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-details" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-connectionDetailsContainer" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-logo" }),
                details))));
});


/***/ }),

/***/ "./lib/components/configuring/choose-bundles.js":
/*!******************************************************!*\
  !*** ./lib/components/configuring/choose-bundles.js ***!
  \******************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ChooseBundles": () => (/* binding */ ChooseBundles)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../store */ "./lib/store.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../common/layout */ "./lib/components/common/layout.js");
/* harmony import */ var _material_ui_core_List__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @material-ui/core/List */ "./node_modules/@material-ui/core/esm/List/List.js");
/* harmony import */ var _material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/ListItem */ "./node_modules/@material-ui/core/esm/ListItem/ListItem.js");
/* harmony import */ var _material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/ListItemIcon */ "./node_modules/@material-ui/core/esm/ListItemIcon/ListItemIcon.js");
/* harmony import */ var _material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @material-ui/core/ListItemText */ "./node_modules/@material-ui/core/esm/ListItemText/ListItemText.js");
/* harmony import */ var _material_ui_icons_PlaylistAddCheck__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/icons/PlaylistAddCheck */ "./node_modules/@material-ui/icons/PlaylistAddCheck.js");
/* harmony import */ var _material_ui_icons_PlaylistAdd__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/icons/PlaylistAdd */ "./node_modules/@material-ui/icons/PlaylistAdd.js");










const ChooseBundles = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    const activeBundles = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.selectedBundles;
    const availableBundles = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.filteredAvailableBundles || [];
    const toggleBundle = (bundleName) => {
        if (activeBundles.indexOf(bundleName) === -1) {
            _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.addBundle(bundleName);
        }
        else {
            _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.removeBundle(bundleName);
        }
    };
    const bundleList = Object.keys(availableBundles).map((bundleName) => {
        const isSelected = activeBundles.indexOf(bundleName) !== -1;
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_4__["default"], { key: bundleName, button: true, selected: isSelected, onClick: () => {
                toggleBundle(bundleName);
            } },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_5__["default"], null, isSelected ? react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_PlaylistAddCheck__WEBPACK_IMPORTED_MODULE_6__["default"], null) : react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_PlaylistAdd__WEBPACK_IMPORTED_MODULE_7__["default"], null)),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_8__["default"], { id: bundleName, primary: bundleName })));
    });
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Section, { title: "Add Configuration Bundle" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_List__WEBPACK_IMPORTED_MODULE_9__["default"], { dense: true, disablePadding: true }, bundleList)));
});


/***/ }),

/***/ "./lib/components/configuring/index.js":
/*!*********************************************!*\
  !*** ./lib/components/configuring/index.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Configuring": () => (/* binding */ Configuring)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_icons_Link__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/icons/Link */ "./node_modules/@material-ui/icons/Link.js");
/* harmony import */ var _material_ui_core_Button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/core/Button */ "./node_modules/@material-ui/core/esm/Button/Button.js");
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../store */ "./lib/store.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../common/layout */ "./lib/components/common/layout.js");
/* harmony import */ var _input_spark_configuration__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./input-spark-configuration */ "./lib/components/configuring/input-spark-configuration.js");
/* harmony import */ var _choose_bundles__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./choose-bundles */ "./lib/components/configuring/choose-bundles.js");
/* harmony import */ var _selected_configuration__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./selected-configuration */ "./lib/components/configuring/selected-configuration.js");








const Configuring = () => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_2__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-scrollable" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_choose_bundles__WEBPACK_IMPORTED_MODULE_4__.ChooseBundles, null),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_input_spark_configuration__WEBPACK_IMPORTED_MODULE_3__.InputSparkConfiguration, null),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_selected_configuration__WEBPACK_IMPORTED_MODULE_5__.SelectedConfiguration, null)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Button__WEBPACK_IMPORTED_MODULE_6__["default"], { color: "primary", variant: "contained", onClick: () => {
                _store__WEBPACK_IMPORTED_MODULE_1__.store.onClickConnect();
            }, startIcon: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Link__WEBPACK_IMPORTED_MODULE_7__["default"], null), className: "jp-SparkConnector-button-main" }, "Connect")));
};


/***/ }),

/***/ "./lib/components/configuring/input-spark-configuration.js":
/*!*****************************************************************!*\
  !*** ./lib/components/configuring/input-spark-configuration.js ***!
  \*****************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "InputSparkConfiguration": () => (/* binding */ InputSparkConfiguration)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/core/TextField */ "./node_modules/@material-ui/core/esm/TextField/TextField.js");
/* harmony import */ var _material_ui_lab_Autocomplete__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/lab/Autocomplete */ "./node_modules/@material-ui/lab/esm/Autocomplete/Autocomplete.js");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @material-ui/core */ "webpack/sharing/consume/default/@material-ui/core/@material-ui/core?e1f9");
/* harmony import */ var _material_ui_core__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../store */ "./lib/store.js");
/* harmony import */ var _material_ui_icons_Add__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/icons/Add */ "./node_modules/@material-ui/icons/Add.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../common/layout */ "./lib/components/common/layout.js");








const InputSparkConfiguration = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_2__.observer)(() => {
    const options = _store__WEBPACK_IMPORTED_MODULE_3__.store.availableOptions || [];
    const [selectedSuggestion, setSelectedSuggestion] = react__WEBPACK_IMPORTED_MODULE_0___default().useState(null);
    const [configurationName, setConfigurationName] = react__WEBPACK_IMPORTED_MODULE_0___default().useState('');
    const [value, setValue] = react__WEBPACK_IMPORTED_MODULE_0___default().useState('');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_4__.Section, { title: "Add Extra Configuration" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", null,
                "You can configure the following",
                ' ',
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { href: "https://spark.apache.org/docs/latest/configuration#available-properties", target: "_blank", rel: "noreferrer" }, "options.")),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", null, "These options override options in the selected bundles."),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", null,
                "Environment variables can be used via ",
                '{ENV_VAR_NAME}',
                ".")),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-input-sparkopts" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_lab_Autocomplete__WEBPACK_IMPORTED_MODULE_5__["default"], { size: "small", freeSolo: true, options: options, inputValue: configurationName, onInputChange: (_, newName) => {
                    setConfigurationName(newName);
                }, value: selectedSuggestion, onChange: (_, newValue) => {
                    setSelectedSuggestion(newValue);
                }, disableClearable: true, groupBy: (option) => option.data.category, getOptionLabel: (option) => {
                    if (typeof option === 'string') {
                        return option;
                    }
                    return option.value;
                }, renderInput: (params) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_6__["default"], Object.assign({}, params, { label: "Configuration Name", variant: "outlined", size: "small" }))) }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_TextField__WEBPACK_IMPORTED_MODULE_6__["default"], { label: "Value", size: "small", variant: "outlined", value: value, onChange: (event) => {
                    setValue(event.target.value);
                } }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core__WEBPACK_IMPORTED_MODULE_1__.Button, { startIcon: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Add__WEBPACK_IMPORTED_MODULE_7__["default"], null), disabled: !configurationName || !value, variant: "contained", onClick: () => {
                    _store__WEBPACK_IMPORTED_MODULE_3__.store.currentNotebook.addConfiguration(configurationName, value);
                    setConfigurationName('');
                    setValue('');
                } }, "Add Configuration"))));
});


/***/ }),

/***/ "./lib/components/configuring/selected-configuration.js":
/*!**************************************************************!*\
  !*** ./lib/components/configuring/selected-configuration.js ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SelectedConfiguration": () => (/* binding */ SelectedConfiguration)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../store */ "./lib/store.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../common/layout */ "./lib/components/common/layout.js");
/* harmony import */ var _material_ui_core_List__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @material-ui/core/List */ "./node_modules/@material-ui/core/esm/List/List.js");
/* harmony import */ var _material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/ListItem */ "./node_modules/@material-ui/core/esm/ListItem/ListItem.js");
/* harmony import */ var _material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/ListItemIcon */ "./node_modules/@material-ui/core/esm/ListItemIcon/ListItemIcon.js");
/* harmony import */ var _material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/core/ListItemText */ "./node_modules/@material-ui/core/esm/ListItemText/ListItemText.js");
/* harmony import */ var _material_ui_core_Collapse__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @material-ui/core/Collapse */ "./node_modules/@material-ui/core/esm/Collapse/Collapse.js");
/* harmony import */ var _material_ui_icons_ExpandLess__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @material-ui/icons/ExpandLess */ "./node_modules/@material-ui/icons/ExpandLess.js");
/* harmony import */ var _material_ui_icons_ExpandMore__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @material-ui/icons/ExpandMore */ "./node_modules/@material-ui/icons/ExpandMore.js");
/* harmony import */ var _material_ui_icons_Settings__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/icons/Settings */ "./node_modules/@material-ui/icons/Settings.js");
/* harmony import */ var _material_ui_icons_Delete__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @material-ui/icons/Delete */ "./node_modules/@material-ui/icons/Delete.js");
/* harmony import */ var _material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @material-ui/core/IconButton */ "./node_modules/@material-ui/core/esm/IconButton/IconButton.js");
/* harmony import */ var _material_ui_core_ListItemSecondaryAction__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @material-ui/core/ListItemSecondaryAction */ "./node_modules/@material-ui/core/esm/ListItemSecondaryAction/ListItemSecondaryAction.js");
/* harmony import */ var _material_ui_core_ListSubheader__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @material-ui/core/ListSubheader */ "./node_modules/@material-ui/core/esm/ListSubheader/ListSubheader.js");
















const SelectedConfigurationItem = (props) => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_4__["default"], { dense: true, key: props.config.id },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_5__["default"], null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Settings__WEBPACK_IMPORTED_MODULE_6__["default"], null)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_7__["default"], { primary: props.config.name, secondary: props.config.value }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemSecondaryAction__WEBPACK_IMPORTED_MODULE_8__["default"], null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_9__["default"], { edge: "end", size: "small", onClick: props.onClickRemove },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Delete__WEBPACK_IMPORTED_MODULE_10__["default"], null)))));
};
const SelectedBundleItem = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)((props) => {
    var _a, _b;
    const [expanded, setExpanded] = react__WEBPACK_IMPORTED_MODULE_0___default().useState(true);
    const configList = (_b = (_a = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.filteredAvailableBundles[props.bundleName]) === null || _a === void 0 ? void 0 : _a.options) === null || _b === void 0 ? void 0 : _b.map((config, index) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_4__["default"], { dense: true, key: index },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_5__["default"], null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Settings__WEBPACK_IMPORTED_MODULE_6__["default"], null)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_7__["default"], { primary: config['name'], secondary: config['value'] }))));
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_4__["default"], { dense: true, button: true, divider: true, onClick: () => {
                setExpanded(!expanded);
            }, key: props.bundleName },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_5__["default"], null,
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_9__["default"], { "aria-label": "delete", size: "small", onClick: () => {
                        _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.removeBundle(props.bundleName);
                    } },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Delete__WEBPACK_IMPORTED_MODULE_10__["default"], null))),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_7__["default"], { primary: react__WEBPACK_IMPORTED_MODULE_0___default().createElement("b", null, props.bundleName) }),
            expanded ? react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_ExpandLess__WEBPACK_IMPORTED_MODULE_11__["default"], null) : react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_ExpandMore__WEBPACK_IMPORTED_MODULE_12__["default"], null)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Collapse__WEBPACK_IMPORTED_MODULE_13__["default"], { in: expanded, timeout: "auto" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_List__WEBPACK_IMPORTED_MODULE_14__["default"], { component: "div", disablePadding: true, dense: true }, configList))));
});
const SelectedConfiguration = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    const bundles = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.selectedBundles.map((bundleName) => {
        return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(SelectedBundleItem, { bundleName: bundleName, key: bundleName });
    });
    const options = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.selectedConfigurations.map((option) => {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(SelectedConfigurationItem, { config: option, onClickRemove: () => {
                _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.removeConfiguration(option.id);
            }, key: option.id }));
    });
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Section, { title: "Selected Configuration", className: "jp-SparkConnector-selected-config" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_List__WEBPACK_IMPORTED_MODULE_14__["default"], { dense: true, disablePadding: true },
            bundles,
            options.length > 0 && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_ListSubheader__WEBPACK_IMPORTED_MODULE_15__["default"], null, "Extra Configuration")),
            options)));
});


/***/ }),

/***/ "./lib/components/connect-failed.js":
/*!******************************************!*\
  !*** ./lib/components/connect-failed.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ConnectFailedComponent": () => (/* binding */ ConnectFailedComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _material_ui_icons_Replay__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @material-ui/icons/Replay */ "./node_modules/@material-ui/icons/Replay.js");
/* harmony import */ var _material_ui_core_Button__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/core/Button */ "./node_modules/@material-ui/core/esm/Button/Button.js");
/* harmony import */ var _material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/lab/Alert */ "./node_modules/@material-ui/lab/esm/Alert/Alert.js");
/* harmony import */ var _material_ui_lab_AlertTitle__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/lab/AlertTitle */ "./node_modules/@material-ui/lab/esm/AlertTitle/AlertTitle.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./common/layout */ "./lib/components/common/layout.js");
/* harmony import */ var _common_loglist__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./common/loglist */ "./lib/components/common/loglist.js");
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../store */ "./lib/store.js");









const ConnectFailedComponent = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_layout__WEBPACK_IMPORTED_MODULE_2__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_layout__WEBPACK_IMPORTED_MODULE_2__.Section, { title: "connection failed", className: "jp-SparkConnector-error" },
            react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_5__["default"], { severity: "error" },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_lab_AlertTitle__WEBPACK_IMPORTED_MODULE_6__["default"], null, "Error"),
                _store__WEBPACK_IMPORTED_MODULE_4__.store.currentNotebook.errorMessage)),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_layout__WEBPACK_IMPORTED_MODULE_2__.Section, { title: "logs", className: "jp-SparkConnector-logs" },
            react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_loglist__WEBPACK_IMPORTED_MODULE_3__.LogList, null)),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_Button__WEBPACK_IMPORTED_MODULE_7__["default"], { color: "secondary", variant: "contained", onClick: () => {
                _store__WEBPACK_IMPORTED_MODULE_4__.store.onClickRestart();
            }, startIcon: react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_icons_Replay__WEBPACK_IMPORTED_MODULE_8__["default"], null), className: "jp-SparkConnector-button-main" }, "Restart")));
});


/***/ }),

/***/ "./lib/components/connected.js":
/*!*************************************!*\
  !*** ./lib/components/connected.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Connected": () => (/* binding */ Connected)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _material_ui_core_List__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/core/List */ "./node_modules/@material-ui/core/esm/List/List.js");
/* harmony import */ var _material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @material-ui/core/ListItem */ "./node_modules/@material-ui/core/esm/ListItem/ListItem.js");
/* harmony import */ var _material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @material-ui/core/ListItemIcon */ "./node_modules/@material-ui/core/esm/ListItemIcon/ListItemIcon.js");
/* harmony import */ var _material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @material-ui/core/ListItemText */ "./node_modules/@material-ui/core/esm/ListItemText/ListItemText.js");
/* harmony import */ var _material_ui_icons_Assessment__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @material-ui/icons/Assessment */ "./node_modules/@material-ui/icons/Assessment.js");
/* harmony import */ var _material_ui_icons_WebAsset__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @material-ui/icons/WebAsset */ "./node_modules/@material-ui/icons/WebAsset.js");
/* harmony import */ var _material_ui_icons_LinkOff__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @material-ui/icons/LinkOff */ "./node_modules/@material-ui/icons/LinkOff.js");
/* harmony import */ var _material_ui_core_Button__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @material-ui/core/Button */ "./node_modules/@material-ui/core/esm/Button/Button.js");
/* harmony import */ var _material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/lab/Alert */ "./node_modules/@material-ui/lab/esm/Alert/Alert.js");
/* harmony import */ var _material_ui_lab_AlertTitle__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/lab/AlertTitle */ "./node_modules/@material-ui/lab/esm/AlertTitle/AlertTitle.js");
/* harmony import */ var _material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @material-ui/core/IconButton */ "./node_modules/@material-ui/core/esm/IconButton/IconButton.js");
/* harmony import */ var _material_ui_icons_Refresh__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @material-ui/icons/Refresh */ "./node_modules/@material-ui/icons/Refresh.js");
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../store */ "./lib/store.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./common/layout */ "./lib/components/common/layout.js");
/* harmony import */ var _common_loglist__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./common/loglist */ "./lib/components/common/loglist.js");

















const YouAreConnecedTo = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_lab_Alert__WEBPACK_IMPORTED_MODULE_5__["default"], { severity: "success", style: { margin: '8px' } },
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_lab_AlertTitle__WEBPACK_IMPORTED_MODULE_6__["default"], null,
            "Connected to ",
            react__WEBPACK_IMPORTED_MODULE_0__.createElement("b", null, _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.clusterName)),
        "Variables available in the notebook",
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("li", null,
            "sc:",
            ' ',
            react__WEBPACK_IMPORTED_MODULE_0__.createElement("a", { href: "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.html#pyspark.SparkContext", target: "_blank", rel: "noreferrer" },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement("u", null,
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement("b", null, "SparkContext")))),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement("li", null,
            "spark:",
            ' ',
            react__WEBPACK_IMPORTED_MODULE_0__.createElement("a", { href: "https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession", target: "_blank", rel: "noreferrer" },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement("u", null,
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement("b", null, "SparkSession"))))));
});
const Connected = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    var _a, _b, _c, _d, _e;
    return (react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(YouAreConnecedTo, null),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Section, { title: "connection resources" },
            react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_List__WEBPACK_IMPORTED_MODULE_7__["default"], { dense: true },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_8__["default"], { button: true, component: "a", target: "_blank", href: (_b = (_a = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook) === null || _a === void 0 ? void 0 : _a.connectionResources) === null || _b === void 0 ? void 0 : _b.sparkHistoryServerUrl },
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_9__["default"], null,
                        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_icons_WebAsset__WEBPACK_IMPORTED_MODULE_10__["default"], null)),
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_11__["default"], { primary: "Spark Web UI" })),
                react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_ListItem__WEBPACK_IMPORTED_MODULE_8__["default"], { button: true, component: "a", target: "_blank", href: (_c = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.connectionResources) === null || _c === void 0 ? void 0 : _c.sparkMetricsUrl, disabled: !((_d = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.connectionResources) === null || _d === void 0 ? void 0 : _d.sparkMetricsUrl) },
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_ListItemIcon__WEBPACK_IMPORTED_MODULE_9__["default"], null,
                        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_icons_Assessment__WEBPACK_IMPORTED_MODULE_12__["default"], null)),
                    react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_ListItemText__WEBPACK_IMPORTED_MODULE_11__["default"], { primary: 'Spark Metrics Dashboard' +
                            (!((_e = _store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.connectionResources) === null || _e === void 0 ? void 0 : _e.sparkMetricsUrl)
                                ? '(bundle not added)'
                                : '') })))),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_layout__WEBPACK_IMPORTED_MODULE_3__.Section, { title: "logs", className: "jp-SparkConnector-logs", extraActions: react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_IconButton__WEBPACK_IMPORTED_MODULE_13__["default"], { size: "small", className: "jp-SparkConnector-logrefresh", onClick: () => {
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.onRefreshLogs();
                } },
                react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_icons_Refresh__WEBPACK_IMPORTED_MODULE_14__["default"], null)) },
            react__WEBPACK_IMPORTED_MODULE_0__.createElement(_common_loglist__WEBPACK_IMPORTED_MODULE_4__.LogList, null)),
        react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_core_Button__WEBPACK_IMPORTED_MODULE_15__["default"], { color: "secondary", variant: "contained", onClick: () => {
                _store__WEBPACK_IMPORTED_MODULE_2__.store.onClickRestart();
            }, startIcon: react__WEBPACK_IMPORTED_MODULE_0__.createElement(_material_ui_icons_LinkOff__WEBPACK_IMPORTED_MODULE_16__["default"], null), className: "jp-SparkConnector-button-main" }, "Disconnect")));
});


/***/ }),

/***/ "./lib/components/connecting.js":
/*!**************************************!*\
  !*** ./lib/components/connecting.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Connecting": () => (/* binding */ Connecting)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _material_ui_core_Button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @material-ui/core/Button */ "./node_modules/@material-ui/core/esm/Button/Button.js");
/* harmony import */ var _material_ui_icons_Cancel__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @material-ui/icons/Cancel */ "./node_modules/@material-ui/icons/Cancel.js");
/* harmony import */ var _material_ui_core_CircularProgress__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @material-ui/core/CircularProgress */ "./node_modules/@material-ui/core/esm/CircularProgress/CircularProgress.js");
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../store */ "./lib/store.js");
/* harmony import */ var _common_loglist__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./common/loglist */ "./lib/components/common/loglist.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./common/layout */ "./lib/components/common/layout.js");








const Connecting = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_4__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_4__.Section, { title: "spark connecting", className: "jp-SparkConnector-loading" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_CircularProgress__WEBPACK_IMPORTED_MODULE_5__["default"], { size: 80 })),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_4__.Section, { title: "logs", className: "jp-SparkConnector-logs" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_loglist__WEBPACK_IMPORTED_MODULE_3__.LogList, null)),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_Button__WEBPACK_IMPORTED_MODULE_6__["default"], { color: "secondary", variant: "contained", onClick: () => {
                _store__WEBPACK_IMPORTED_MODULE_2__.store.onClickRestart();
            }, startIcon: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_icons_Cancel__WEBPACK_IMPORTED_MODULE_7__["default"], null), className: "jp-SparkConnector-button-main" }, "Cancel")));
});


/***/ }),

/***/ "./lib/components/loading.js":
/*!***********************************!*\
  !*** ./lib/components/loading.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Loading": () => (/* binding */ Loading)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core_CircularProgress__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @material-ui/core/CircularProgress */ "./node_modules/@material-ui/core/esm/CircularProgress/CircularProgress.js");
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./common/layout */ "./lib/components/common/layout.js");



const Loading = () => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_1__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-loading" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_CircularProgress__WEBPACK_IMPORTED_MODULE_2__["default"], { size: 80 }))));
};


/***/ }),

/***/ "./lib/components/not-attached.js":
/*!****************************************!*\
  !*** ./lib/components/not-attached.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotAttached": () => (/* binding */ NotAttached)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _common_layout__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./common/layout */ "./lib/components/common/layout.js");


const NotAttached = () => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_common_layout__WEBPACK_IMPORTED_MODULE_1__.Layout, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: "jp-SparkConnector-notattached" }, "Open a notebook to connect to Apache Spark")));
};


/***/ }),

/***/ "./lib/components/panel.js":
/*!*********************************!*\
  !*** ./lib/components/panel.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../store */ "./lib/store.js");
/* harmony import */ var _theme_provider__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./theme-provider */ "./lib/components/theme-provider.js");
/* harmony import */ var _authenticate__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./authenticate */ "./lib/components/authenticate.js");
/* harmony import */ var _configuring__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./configuring */ "./lib/components/configuring/index.js");
/* harmony import */ var _connected__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./connected */ "./lib/components/connected.js");
/* harmony import */ var _connect_failed__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./connect-failed */ "./lib/components/connect-failed.js");
/* harmony import */ var _connecting__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./connecting */ "./lib/components/connecting.js");
/* harmony import */ var _loading__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./loading */ "./lib/components/loading.js");
/* harmony import */ var _not_attached__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./not-attached */ "./lib/components/not-attached.js");











const SparkConnectorPanel = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)(() => {
    let page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null);
    if (!_store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook) {
        return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_not_attached__WEBPACK_IMPORTED_MODULE_10__.NotAttached, null);
    }
    switch (_store__WEBPACK_IMPORTED_MODULE_2__.store.currentNotebook.status) {
        case 'configuring':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_configuring__WEBPACK_IMPORTED_MODULE_5__.Configuring, null);
            break;
        case 'auth':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_authenticate__WEBPACK_IMPORTED_MODULE_4__.Authenticate, null);
            break;
        case 'connected':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_connected__WEBPACK_IMPORTED_MODULE_6__.Connected, null);
            break;
        case 'connecting':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_connecting__WEBPACK_IMPORTED_MODULE_8__.Connecting, null);
            break;
        case 'loading':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_loading__WEBPACK_IMPORTED_MODULE_9__.Loading, null);
            break;
        case 'error':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_connect_failed__WEBPACK_IMPORTED_MODULE_7__.ConnectFailedComponent, null);
            break;
        case 'notattached':
            page = react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_loading__WEBPACK_IMPORTED_MODULE_9__.Loading, null);
            break;
    }
    return react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_theme_provider__WEBPACK_IMPORTED_MODULE_3__.ThemeProvider, null, page);
});
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (SparkConnectorPanel);


/***/ }),

/***/ "./lib/components/theme-provider.js":
/*!******************************************!*\
  !*** ./lib/components/theme-provider.js ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ThemeProvider": () => (/* binding */ ThemeProvider)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/core/esm/styles/createTheme.js");
/* harmony import */ var _material_ui_core_styles__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @material-ui/core/styles */ "./node_modules/@material-ui/styles/esm/ThemeProvider/ThemeProvider.js");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! mobx-react-lite */ "webpack/sharing/consume/default/mobx-react-lite/mobx-react-lite");
/* harmony import */ var mobx_react_lite__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../store */ "./lib/store.js");




const brandColor1 = getComputedStyle(document.body)
    .getPropertyValue('--jp-brand-color1')
    .trim();
const createTheme = (color) => {
    return (0,_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_3__.createMuiTheme)({
        shadows: Array(25).fill('none'),
        shape: {
            borderRadius: 2,
        },
        typography: {
            fontSize: 12,
            fontFamily: [
                '-apple-system',
                'BlinkMacSystemFont',
                '"Segoe UI"',
                'Roboto',
                '"Helvetica Neue"',
                'Arial',
                'sans-serif',
                '"Apple Color Emoji"',
                '"Segoe UI Emoji"',
                '"Segoe UI Symbol"',
            ].join(','),
        },
        palette: {
            type: color || 'light',
            primary: {
                main: brandColor1,
            },
        },
    });
};
const lightTheme = createTheme('light');
const darkTheme = createTheme('dark');
const ThemeProvider = (0,mobx_react_lite__WEBPACK_IMPORTED_MODULE_1__.observer)((props) => {
    const currentTheme = _store__WEBPACK_IMPORTED_MODULE_2__.store.colorTheme === 'light' ? lightTheme : darkTheme;
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_material_ui_core_styles__WEBPACK_IMPORTED_MODULE_4__["default"], { theme: currentTheme }, props.children));
});


/***/ })

}]);
//# sourceMappingURL=sparkconnectorui.927c2e5eaf7fd43b5a9b.js.map
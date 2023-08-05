"use strict";
(self["webpackChunk_swan_cern_sparkconnector"] = self["webpackChunk_swan_cern_sparkconnector"] || []).push([["lib_index_js"],{

/***/ "./lib/components/lazy-panel.js":
/*!**************************************!*\
  !*** ./lib/components/lazy-panel.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "LazySparkConnectorPanel": () => (/* binding */ LazySparkConnectorPanel)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

const SparkConnectorPanel = react__WEBPACK_IMPORTED_MODULE_0___default().lazy(() => Promise.all(/*! import() | sparkconnectorui */[__webpack_require__.e("vendors-node_modules_material-ui_core_esm_Button_Button_js-node_modules_material-ui_core_esm_-8bd9ad"), __webpack_require__.e("vendors-node_modules_material-ui_icons_Add_js-node_modules_material-ui_icons_Assessment_js-no-897c3d"), __webpack_require__.e("webpack_sharing_consume_default_react-dom"), __webpack_require__.e("sparkconnectorui")]).then(__webpack_require__.bind(__webpack_require__, /*! ./panel */ "./lib/components/panel.js")));
const LazySparkConnectorPanel = () => {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react__WEBPACK_IMPORTED_MODULE_0__.Suspense, { fallback: react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null, "loading") },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(SparkConnectorPanel, null)));
};


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./store */ "./lib/store.js");
/* harmony import */ var _components_lazy_panel__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./components/lazy-panel */ "./lib/components/lazy-panel.js");
/* harmony import */ var _labconnector__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./labconnector */ "./lib/labconnector.js");
/* harmony import */ var _style_apachespark_svg__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../style/apachespark.svg */ "./style/apachespark.svg");









/**
 * Initialization data for the sparkconnector extension.
 */
const plugin = {
    id: 'sparkconnector',
    requires: [_jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILabShell, _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_1__.INotebookTracker, _jupyterlab_application__WEBPACK_IMPORTED_MODULE_0__.ILayoutRestorer],
    optional: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.IThemeManager],
    activate: activate,
    autoStart: true,
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);
/**
 * Activate the running plugin.
 */
function activate(app, labShell, notebooks, restorer, themeManager) {
    const appConnector = new _labconnector__WEBPACK_IMPORTED_MODULE_7__.JupyterLabConnector(app, notebooks);
    _store__WEBPACK_IMPORTED_MODULE_5__.store.setAppConnector(appConnector);
    const panelWidget = _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_4___default().createElement(_components_lazy_panel__WEBPACK_IMPORTED_MODULE_6__.LazySparkConnectorPanel));
    panelWidget.id = 'spark-connector';
    panelWidget.title.caption = 'Apache Spark';
    panelWidget.title.icon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.LabIcon({
        name: 'sparkconnector:sparkicon',
        svgstr: _style_apachespark_svg__WEBPACK_IMPORTED_MODULE_8__["default"],
    });
    labShell.add(panelWidget, 'right', {
        rank: 700,
    });
    if (themeManager) {
        if (themeManager.theme && themeManager.isLight(themeManager.theme)) {
            _store__WEBPACK_IMPORTED_MODULE_5__.store.colorTheme = 'light';
        }
        else {
            _store__WEBPACK_IMPORTED_MODULE_5__.store.colorTheme = 'dark';
        }
        themeManager.themeChanged.connect((_, args) => {
            if (themeManager.isLight(args.newValue)) {
                _store__WEBPACK_IMPORTED_MODULE_5__.store.colorTheme = 'light';
            }
            else {
                _store__WEBPACK_IMPORTED_MODULE_5__.store.colorTheme = 'dark';
            }
        });
    }
    console.log('SparkConnector: Jupyter Lab extension is activated!');
}


/***/ }),

/***/ "./lib/labconnector.js":
/*!*****************************!*\
  !*** ./lib/labconnector.js ***!
  \*****************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JupyterLabConnector": () => (/* binding */ JupyterLabConnector)
/* harmony export */ });
/* harmony import */ var mobx__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! mobx */ "webpack/sharing/consume/default/mobx/mobx?f37f");
/* harmony import */ var mobx__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(mobx__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _store__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./store */ "./lib/store.js");



const SPARKCONNECTOR_COMM_TARGET = 'SparkConnector';
/*
  Jupyterlab specific integration.
*/
class JupyterLabConnector {
    constructor(labApp, notebookTracker) {
        Object.defineProperty(this, "labApp", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: labApp
        });
        Object.defineProperty(this, "notebookTracker", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: notebookTracker
        });
        /*
          Mapping between notebookPanel Ids to Comm objects
          opened in the kernel for that object.
        */
        Object.defineProperty(this, "comms", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: new Map()
        });
        this.initConfigurationFromServer();
        this.initStateHandling();
    }
    async initConfigurationFromServer() {
        const availableOptionConfigSection = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ConfigSection.create({
            name: 'sparkconnector_spark_options',
        });
        const bundlesConfigSection = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ConfigSection.create({
            name: 'sparkconnector_bundles',
        });
        _store__WEBPACK_IMPORTED_MODULE_2__.store.updateConfigurationFromServer(availableOptionConfigSection.data, bundlesConfigSection.data);
    }
    getNotebookPanel(notebookPanelId) {
        const notebookPanel = this.notebookTracker.find((nb) => nb.id === notebookPanelId);
        if (!notebookPanel) {
            throw new Error('SparkConnector: Notebook Panel does not exist');
        }
        return notebookPanel;
    }
    createComm(notebookPanel) {
        var _a;
        const kernel = (_a = notebookPanel.sessionContext.session) === null || _a === void 0 ? void 0 : _a.kernel;
        if (!kernel) {
            throw new Error('SparkConnector: Trying to create comm when kernel/session is null');
        }
        console.log('SparkConnector: CREATE COMM for ', notebookPanel.title.label, kernel.id);
        const comm = kernel.createComm(SPARKCONNECTOR_COMM_TARGET);
        this.comms.set(notebookPanel.id, comm);
        comm.open({
            type: 'action',
            action: 'sparkconn-action-open',
        });
        comm.onClose = () => {
            this.comms.delete(notebookPanel.id);
            (0,mobx__WEBPACK_IMPORTED_MODULE_0__.runInAction)(() => {
                _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'notattached';
            });
            console.log('SparkConnector: Comm closed:', notebookPanel.title.label);
        };
        comm.onMsg = (msg) => {
            this.handleCommMessage(msg, notebookPanel);
        };
    }
    async trackNotebook(notebookPanel) {
        if (!_store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id]) {
            // If we don't already have a stored state for this notebook:
            _store__WEBPACK_IMPORTED_MODULE_2__.store.createNotebookState(notebookPanel.id, {
                title: notebookPanel.title.label,
            });
        }
        // Ensure the state of the jupyterlab kernel/session object is synced with API
        await notebookPanel.sessionContext.ready;
        // Connect to kernel on first page load
        if (!this.comms.has(notebookPanel.id)) {
            try {
                this.createComm(notebookPanel);
            }
            catch (e) {
                console.error('SparkConnector: Error creating comm');
            }
        }
        // Connect to kernel when a restarting etc.
        // The statusChanged.connect is no-op if already connected.
        notebookPanel.sessionContext.statusChanged.connect((_, status) => {
            switch (status) {
                case 'restarting':
                case 'terminating':
                case 'autorestarting':
                case 'dead':
                case 'unknown':
                    this.comms.delete(notebookPanel.id);
                    (0,mobx__WEBPACK_IMPORTED_MODULE_0__.runInAction)(() => {
                        _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'notattached';
                    });
                    break;
                case 'starting':
                    if (!this.comms.has(notebookPanel.id)) {
                        try {
                            this.createComm(notebookPanel);
                        }
                        catch (e) {
                            console.error('SparkConnector: Error creating comm');
                        }
                    }
                    break;
            }
        }, this);
    }
    initStateHandling() {
        this.notebookTracker.widgetAdded.connect((_, notebookPanel) => {
            this.trackNotebook(notebookPanel);
        });
        this.notebookTracker.currentChanged.connect((_, notebookPanel) => {
            if (!notebookPanel) {
                // There is no notebook panel selected
                _store__WEBPACK_IMPORTED_MODULE_2__.store.setActiveNotebook(null);
            }
            else {
                _store__WEBPACK_IMPORTED_MODULE_2__.store.setActiveNotebook(notebookPanel.id);
            }
        });
    }
    /*
      Handle messages from the Kernel extension.
    */
    handleCommMessage(message, notebookPanel) {
        (0,mobx__WEBPACK_IMPORTED_MODULE_0__.runInAction)(() => {
            const data = message.content.data;
            switch (data.msgtype) {
                case 'sparkconn-action-open': {
                    const page = message.content.data.page;
                    const savedConfig = this.getSavedConfigFromNotebookMetadata(notebookPanel);
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.setNotebookConfig(notebookPanel.id, {
                        maxMemory: data.maxmemory,
                        sparkVersion: data.sparkversion,
                        clusterName: data.cluster,
                        savedConfig,
                    });
                    if (page === 'sparkconn-config') {
                        _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'configuring';
                    }
                    else if (page === 'sparkconn-auth') {
                        _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'auth';
                    }
                    else if (page === 'sparkconn-connected') {
                        // The kernel sends this page when a comm is opened, but the
                        // user is already connected. It subsequently also sends a msgtype: sparkconn-connected,
                        // so we don't do anything here
                    }
                    else {
                        console.log('SparkConnector: Unknown page from server');
                    }
                    break;
                }
                case 'sparkconn-connected': {
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].connectionResources = {
                        sparkHistoryServerUrl: data.config.sparkhistoryserver,
                        sparkMetricsUrl: data.config.sparkmetrics,
                    };
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'connected';
                    break;
                }
                case 'sparkconn-config': {
                    // Sent by kernel on successful authentication
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'configuring';
                    break;
                }
                case 'sparkconn-auth': {
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'auth';
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].authError = data.error;
                    break;
                }
                case 'sparkconn-connect-error': {
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].errorMessage = data.error;
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.notebooks[notebookPanel.id].status = 'error';
                    break;
                }
                case 'sparkconn-action-follow-log': {
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.appendConnectionLog(notebookPanel.id, data.msg);
                    break;
                }
                case 'sparkconn-action-tail-log': {
                    _store__WEBPACK_IMPORTED_MODULE_2__.store.updateLogs(notebookPanel.id, data.msg);
                    break;
                }
                default:
                    console.error('SparkConnector: Received an unknown msgtype from kernel:', message);
                    break;
            }
        });
    }
    onClickAuthenticate(notebookPanelId, password) {
        const comm = this.comms.get(notebookPanelId);
        if (comm) {
            comm.send({
                action: 'sparkconn-action-auth',
                password,
            });
        }
    }
    onClickConnect(notebookPanelId, options) {
        const comm = this.comms.get(notebookPanelId);
        if (comm) {
            comm.send({
                action: 'sparkconn-action-connect',
                options,
            });
        }
    }
    async promptUserForKernelRestart(notebookPanelId) {
        return this.labApp.commands.execute('notebook:restart-kernel');
    }
    async onClickRestart(notebookPanelId) {
        // Restart the kernel, because SparkContexts are cached,
        // we need to restart to do a clean retry again
        const isRestarted = await this.promptUserForKernelRestart(notebookPanelId);
        if (isRestarted) {
            const comm = this.comms.get(notebookPanelId);
            if (comm) {
                comm.send({
                    action: 'sparkconn-action-disconnect',
                });
            }
        }
    }
    onRefreshLogs(notebookPanelId) {
        const comm = this.comms.get(notebookPanelId);
        if (comm) {
            comm.send({
                action: 'sparkconn-action-getlogs',
            });
        }
    }
    getSavedConfigFromNotebookMetadata(notebookPanel) {
        var _a;
        let currentConfig;
        if ((_a = notebookPanel.model) === null || _a === void 0 ? void 0 : _a.metadata.has('sparkconnect')) {
            currentConfig = notebookPanel.model.metadata.get('sparkconnect');
        }
        else {
            currentConfig = {
                bundled_options: [],
                list_of_options: [],
            };
        }
        // TODO silently remove any bundles that are not in the current set.
        return currentConfig;
    }
    saveCurrentConfigToNotebookMetadata(notebookPanelId, config) {
        var _a;
        const notebookPanel = this.getNotebookPanel(notebookPanelId);
        (_a = notebookPanel.model) === null || _a === void 0 ? void 0 : _a.metadata.set('sparkconnect', config);
    }
}


/***/ }),

/***/ "./lib/store.js":
/*!**********************!*\
  !*** ./lib/store.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "store": () => (/* binding */ store)
/* harmony export */ });
/* harmony import */ var mobx__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! mobx */ "webpack/sharing/consume/default/mobx/mobx?f37f");
/* harmony import */ var mobx__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(mobx__WEBPACK_IMPORTED_MODULE_0__);

let uniqueId = 0;
/*
  An observable MobX store.

  React components wrapped with observer() are automatically re-rendered
  when the store data is changed.

  All updates to the store must either be methods on this class or
  be wrapped in action(). See MobX documentation for details.
*/
class SparkConnectorStore {
    constructor() {
        Object.defineProperty(this, "colorTheme", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'light'
        });
        Object.defineProperty(this, "notebooks", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: {}
        });
        Object.defineProperty(this, "allAvailableBundles", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: {}
        });
        Object.defineProperty(this, "availableOptions", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: []
        });
        Object.defineProperty(this, "currentNotebookPanelId", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: null
        });
        Object.defineProperty(this, "appConnector", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        (0,mobx__WEBPACK_IMPORTED_MODULE_0__.makeAutoObservable)(this);
    }
    setAppConnector(connector) {
        this.appConnector = connector;
    }
    updateConfigurationFromServer(sparkOptionsData, bundleData) {
        this.allAvailableBundles = bundleData.bundled_options || {};
        const sparkOptions = (sparkOptionsData === null || sparkOptionsData === void 0 ? void 0 : sparkOptionsData.spark_options) || [];
        // Sort the options alphabetically based on category
        // for auto-complete to work
        sparkOptions.sort((a, b) => {
            return a.data.category.localeCompare(b.data.category);
        });
        this.availableOptions = sparkOptions;
    }
    /*
      Computed/Derived values from the state
    */
    get currentNotebook() {
        return this.notebooks[this.currentNotebookPanelId];
    }
    /*
      Actions that modify the state
    */
    createNotebookState(notebookPanelId, options) {
        const notebookState = new NotebookStateStore();
        notebookState.title = options.title;
        notebookState.status = 'notattached';
        this.notebooks[notebookPanelId] = notebookState;
        this.currentNotebookPanelId = notebookPanelId;
    }
    setActiveNotebook(notebookPanelId) {
        this.currentNotebookPanelId = notebookPanelId;
    }
    deleteNotebookState(notebookPanelId) {
        delete this.notebooks[notebookPanelId];
        if ((this.currentNotebookPanelId = notebookPanelId)) {
            this.currentNotebookPanelId = null;
        }
    }
    setNotebookConfig(notebookPanelId, options) {
        var _a, _b, _c;
        this.notebooks[notebookPanelId].clusterName = options.clusterName;
        this.notebooks[notebookPanelId].sparkVersion = options.sparkVersion;
        this.notebooks[notebookPanelId].maxMemory = options.maxMemory;
        this.notebooks[notebookPanelId].selectedConfigurations = [];
        this.notebooks[notebookPanelId].selectedBundles = [];
        (_a = options === null || options === void 0 ? void 0 : options.savedConfig) === null || _a === void 0 ? void 0 : _a.bundled_options.forEach((bundleName) => {
            // Ignore any bundles not in our current configuration and not available for the selected cluster/session
            if (this.allAvailableBundles[bundleName] &&
                this.notebooks[notebookPanelId].filteredAvailableBundles[bundleName]) {
                this.notebooks[notebookPanelId].selectedBundles.push(bundleName);
            }
        });
        (_c = (_b = options === null || options === void 0 ? void 0 : options.savedConfig) === null || _b === void 0 ? void 0 : _b.list_of_options) === null || _c === void 0 ? void 0 : _c.forEach((config) => {
            this.notebooks[notebookPanelId].selectedConfigurations.push({
                id: `${++uniqueId}`,
                name: config.name,
                value: config.value,
                isEnabled: config.isEnabled !== undefined ? config.isEnabled : true,
            });
        });
    }
    appendConnectionLog(notebookPanelId, message) {
        this.notebooks[notebookPanelId].logs.push(message);
    }
    updateLogs(notebookPanelId, logs) {
        this.notebooks[notebookPanelId].logs = logs;
    }
    onClickConnect() {
        var _a, _b;
        if (!this.currentNotebookPanelId) {
            throw Error('SparkConnector: Inconsistent state. Attempting to connect with no active notebook.');
        }
        console.log('SparkConnector: Connecting to Spark', this.currentNotebook.optionsToSendToKernel);
        store.currentNotebook.status = 'connecting';
        store.currentNotebook.logs = ['Waiting for spark context to start'];
        const notebookMetadata = {
            bundled_options: store.currentNotebook.selectedBundles,
            list_of_options: store.currentNotebook.selectedConfigurations.map((c) => ({
                name: c.name,
                value: c.value,
            })),
        };
        (_a = this.appConnector) === null || _a === void 0 ? void 0 : _a.saveCurrentConfigToNotebookMetadata(this.currentNotebookPanelId, notebookMetadata);
        (_b = this.appConnector) === null || _b === void 0 ? void 0 : _b.onClickConnect(this.currentNotebookPanelId, this.currentNotebook.optionsToSendToKernel);
    }
    onClickAuthenticate(password) {
        var _a;
        this.currentNotebook.status = 'loading';
        store.currentNotebook.authError = undefined;
        (_a = this.appConnector) === null || _a === void 0 ? void 0 : _a.onClickAuthenticate(this.currentNotebookPanelId, password);
    }
    onClickRestart() {
        var _a;
        (_a = this.appConnector) === null || _a === void 0 ? void 0 : _a.onClickRestart(store.currentNotebookPanelId);
    }
    onRefreshLogs() {
        var _a;
        (_a = this.appConnector) === null || _a === void 0 ? void 0 : _a.onRefreshLogs(this.currentNotebookPanelId);
    }
}
class NotebookStateStore {
    constructor() {
        Object.defineProperty(this, "title", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "maxMemory", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "sparkVersion", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "clusterName", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "authError", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "status", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: 'configuring'
        });
        Object.defineProperty(this, "selectedConfigurations", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: []
        });
        Object.defineProperty(this, "selectedBundles", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: []
        });
        Object.defineProperty(this, "errorMessage", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "connectionResources", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: void 0
        });
        Object.defineProperty(this, "logs", {
            enumerable: true,
            configurable: true,
            writable: true,
            value: []
        });
        (0,mobx__WEBPACK_IMPORTED_MODULE_0__.makeAutoObservable)(this);
    }
    get filteredAvailableBundles() {
        const filteredBundles = {};
        Object.keys(store.allAvailableBundles).forEach((bundleName) => {
            const bundle = store.allAvailableBundles[bundleName];
            const isNotEnabledForCluster = bundle.cluster_filter &&
                bundle.cluster_filter.length !== 0 &&
                !bundle.cluster_filter.includes(this.clusterName);
            const isNotEnabledForSparkVersion = bundle.spark_version_filter &&
                bundle.spark_version_filter.length !== 0 &&
                !bundle.spark_version_filter.includes(this.sparkVersion);
            if (!(isNotEnabledForCluster || isNotEnabledForSparkVersion)) {
                filteredBundles[bundleName] = bundle;
            }
        });
        return filteredBundles;
    }
    get optionsToSendToKernel() {
        const options = {};
        this.selectedConfigurations.forEach((configuration) => {
            if (configuration.isEnabled) {
                options[configuration.name] = configuration.value;
            }
        });
        // here the bundles are merged with the user configurations:
        // - if key in bundle does not exist already, it is created
        // - if it exists already, we check the "concatenate" value:
        //   - if it exists, we use it to concatenate to the existing conf,
        //   - otherwise we don't add it: the choices of the user have higher priority
        this.selectedBundles.forEach((bundleName) => {
            this.filteredAvailableBundles[bundleName].options.forEach((bundleOption) => {
                if (bundleOption['name'] in options) {
                    if (bundleOption['concatenate'] &&
                        bundleOption['concatenate'] !== '') {
                        options[bundleOption['name']] =
                            options[bundleOption['name']] +
                                bundleOption['concatenate'] +
                                bundleOption['value'];
                    } //else we don't add it
                }
                else {
                    //we create the new option
                    options[bundleOption['name']] = bundleOption['value'];
                }
            });
        });
        return options;
    }
    addConfiguration(name, value) {
        this.selectedConfigurations.push({
            id: `${++uniqueId}`,
            name,
            value,
            isEnabled: true,
        });
    }
    removeConfiguration(id) {
        const index = this.selectedConfigurations.findIndex((c) => c.id === id);
        if (index > -1) {
            this.selectedConfigurations.splice(index, 1);
        }
    }
    addBundle(bundleName) {
        this.selectedBundles.push(bundleName);
    }
    removeBundle(bundleName) {
        const index = this.selectedBundles.indexOf(bundleName);
        if (index > -1) {
            this.selectedBundles.splice(index, 1);
        }
    }
}
const store = new SparkConnectorStore();
// For debugging
window.sparkConnectorStore = store;


/***/ }),

/***/ "./style/apachespark.svg":
/*!*******************************!*\
  !*** ./style/apachespark.svg ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg fill=\"#616161\" class=\"jp-icon3\" role=\"img\" viewBox=\"0 0 24 24\" xmlns=\"http://www.w3.org/2000/svg\"><title>Apache Spark</title><path d=\"M10.812 0c-.425.013-.845.215-1.196.605a3.593 3.593 0 00-.493.722c-.355.667-.425 1.415-.556 2.143a551.9 551.9 0 00-.726 4.087c-.027.16-.096.227-.244.273C5.83 8.386 4.06 8.94 2.3 9.514c-.387.125-.773.289-1.114.506-1.042.665-1.196 1.753-.415 2.71.346.422.79.715 1.284.936 1.1.49 2.202.976 3.3 1.47.019.01.036.013.053.019h-.004l1.306.535c0 .023.002.045 0 .073-.2 2.03-.39 4.063-.58 6.095-.04.419-.012.831.134 1.23.317.87 1.065 1.148 1.881.701.372-.204.666-.497.937-.818 1.372-1.623 2.746-3.244 4.113-4.872.111-.133.205-.15.363-.098.349.117.697.231 1.045.347h.001c.02.012.045.02.073.03l.142.042c1.248.416 2.68.775 3.929 1.19.4.132.622.164 1.045.098.311-.048.592-.062.828-.236.602-.33.995-.957.988-1.682-.005-.427-.154-.813-.35-1.186-.82-1.556-1.637-3.113-2.461-4.666-.078-.148-.076-.243.037-.375 1.381-1.615 2.756-3.236 4.133-4.855.272-.32.513-.658.653-1.058.308-.878-.09-1.57-1-1.741a2.783 2.783 0 00-1.235.069c-1.974.521-3.947 1.041-5.918 1.57-.175.047-.26.015-.355-.144a353.08 353.08 0 00-2.421-4.018 4.61 4.61 0 00-.652-.849c-.371-.37-.802-.549-1.227-.536zm.172 3.703a.592.592 0 01.189.211c.87 1.446 1.742 2.89 2.609 4.338.07.118.135.16.277.121 1.525-.41 3.052-.813 4.579-1.217.367-.098.735-.193 1.103-.289a.399.399 0 01-.1.2c-1.259 1.48-2.516 2.962-3.779 4.438-.11.13-.12.22-.04.37.937 1.803 1.768 3.309 2.498 4.76l-3.696-1.019c-.538-.18-1.077-.358-1.615-.539-.163-.055-.25-.03-.36.1-1.248 1.488-2.504 2.97-3.759 4.454a.398.398 0 01-.18.132c.035-.378.068-.757.104-1.136.149-1.572.297-3.144.451-4.716-.03-.318.117-.405-.322-.545-1.493-.593-3.346-1.321-4.816-1.905a.595.595 0 01.24-.134c1.797-.57 3.595-1.14 5.394-1.705.127-.04.199-.092.211-.233.013-.148.05-.294.076-.441.241-1.363.483-2.726.726-4.088.068-.386.14-.771.21-1.157z\"/></svg>");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.8f0d5ad88f2ed3be758e.js.map
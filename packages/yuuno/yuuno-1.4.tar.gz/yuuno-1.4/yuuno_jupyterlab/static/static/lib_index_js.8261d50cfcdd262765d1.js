"use strict";
(self["webpackChunk_yuuno_jupyterlab"] = self["webpackChunk_yuuno_jupyterlab"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/settingregistry */ "webpack/sharing/consume/default/@jupyterlab/settingregistry");
/* harmony import */ var _jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
/* harmony import */ var _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _widgets_preview_index__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./widgets/preview/index */ "./lib/widgets/preview/index.js");
/* harmony import */ var _widgets_encode_index__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./widgets/encode/index */ "./lib/widgets/encode/index.js");
/* harmony import */ var _widgets_audio_index__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./widgets/audio/index */ "./lib/widgets/audio/index.js");





/**
 * Initialization data for the @yuuno/jupyterlab extension.
 */
const plugin = {
    id: '@yuuno/jupyterlab:plugin',
    autoStart: true,
    requires: [_jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_1__.IJupyterWidgetRegistry],
    optional: [_jupyterlab_settingregistry__WEBPACK_IMPORTED_MODULE_0__.ISettingRegistry],
    activate: (app, widgets, settingRegistry) => {
        console.log('JupyterLab extension @yuuno/jupyterlab is activated!');
        widgets.registerWidget({
            name: "@yuuno/jupyter",
            version: "1.2.0",
            exports: {
                PreviewWindowWidget: _widgets_preview_index__WEBPACK_IMPORTED_MODULE_2__.PreviewWindowWidget,
                EncodeWindowWidget: _widgets_encode_index__WEBPACK_IMPORTED_MODULE_3__.EncodeWindowWidget,
                AudioPlaybackWidget: _widgets_audio_index__WEBPACK_IMPORTED_MODULE_4__.AudioPlaybackWidget
            }
        });
        console.log('@yuuno/jupyterlab: Widgets registered.');
        if (settingRegistry) {
            settingRegistry
                .load(plugin.id)
                .then(settings => {
                console.log('@yuuno/jupyterlab settings loaded:', settings.composite);
            })
                .catch(reason => {
                console.error('Failed to load settings for @yuuno/jupyterlab.', reason);
            });
        }
        // requestAPI<any>('get_example')
        //   .then(data => {
        //     console.log(data);
        //   })
        //   .catch(reason => {
        //     console.error(
        //       `The yuuno_jupyterlab server extension appears to be missing.\n${reason}`
        //     );
        //   });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/model-rpc.js":
/*!**************************!*\
  !*** ./lib/model-rpc.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "WidgetChannel": () => (/* binding */ WidgetChannel)
/* harmony export */ });
class WidgetChannel {
    constructor(model) {
        this.model = model;
    }
    /**
     * Sends a message through this channel.
     */
    async send(message) {
        const buffers = ("buffers" in message ? message.buffers : []) || [];
        if ("buffers" in message)
            delete message["buffers"];
        this.model.send(message, buffers);
    }
    /**
     * Subscribe to messages.
     */
    subscribe(subscriber) {
        const cb = (content, buffers) => {
            if (buffers.length > 0) {
                content.buffers = buffers.map((b) => {
                    if (b instanceof ArrayBuffer) {
                        return b;
                    }
                    else {
                        var dst = new ArrayBuffer(b.byteLength);
                        new Uint8Array(dst).set(new Uint8Array(b.buffer));
                        return dst;
                    }
                });
            }
            subscriber(content);
        };
        this.model.on("msg:custom", cb);
        return () => {
            this.model.off("msg:custom", cb);
        };
    }
    ;
}


/***/ }),

/***/ "./lib/rpc.js":
/*!********************!*\
  !*** ./lib/rpc.js ***!
  \********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RPCServer": () => (/* binding */ RPCServer),
/* harmony export */   "RPCClient": () => (/* binding */ RPCClient),
/* harmony export */   "timeout": () => (/* binding */ timeout),
/* harmony export */   "race": () => (/* binding */ race)
/* harmony export */ });
let _instance_counter = 0;
class RPCServer {
    constructor(functions, channel) {
        this.functions = functions;
        this.channel = channel;
        this.subscription = null;
    }
    _closeSubscription() {
        if (this.subscription !== null) {
            this.subscription();
            this.subscription = null;
        }
    }
    open() {
        this._closeSubscription();
        this.subscription = this.channel.subscribe((p) => this._receive(p).catch(console.log));
    }
    close() {
        this._closeSubscription();
    }
    async _send(packet) {
        if (this.subscription === null)
            return;
        this.channel.send(packet);
    }
    async _receive(packet) {
        if (!packet.id) {
            await this._send({
                id: "",
                type: "failure",
                payload: "Unknown ID"
            });
            return;
        }
        if (!packet.type) {
            await this._send({
                id: packet.id,
                type: "failure",
                payload: "No method called."
            });
            return;
        }
        if (!(packet.type in this.functions)) {
            await this._send({
                id: packet.id,
                type: "failure",
                payload: "Unknown method."
            });
            return;
        }
        let input_buffers = [];
        if (!!packet.buffers) {
            input_buffers = packet.buffers;
            delete packet.buffers;
        }
        let result = undefined;
        try {
            let raw_result = this.functions[packet.type];
            let p_result = raw_result(packet.payload, input_buffers);
            if ("then" in p_result)
                result = await p_result;
            else
                result = raw_result;
        }
        catch (e) {
            await this._send({
                id: packet.id,
                type: "failure",
                payload: e.toString()
            });
            return;
        }
        let buffers = [];
        if ("buffers" in result) {
            buffers = result.buffers;
            delete result["buffers"];
        }
        await this._send({
            id: packet.id,
            type: "response",
            payload: result,
            buffers: buffers
        });
    }
}
class RPCClient {
    constructor(channel) {
        this._requests = new Map();
        this._instance_number = _instance_counter++;
        this._current_packet_counter = 0;
        this.channel = channel;
        this.subscription = null;
    }
    _closeSubscription() {
        if (this.subscription !== null) {
            this.subscription();
            this.subscription = null;
        }
    }
    open() {
        this._closeSubscription();
        this.subscription = this.channel.subscribe((pkt) => this._receive(pkt));
    }
    _receive(packet) {
        // Drop packets not for us.
        if (!this._requests.has(packet.id))
            return;
        const awaiter = this._requests.get(packet.id);
        this._requests.delete(packet.id);
        awaiter(packet);
    }
    makeProxy(cancel) {
        const cache = {
            open: () => this.open(),
            close: () => this.close()
        };
        return new Proxy(cache, {
            get: (_, name) => {
                return name in cache
                    ? cache[name]
                    : (cache[name] = (payload = {}, buffers = undefined) => {
                        return this.request(name.toString(), payload, buffers, cancel);
                    });
            }
        });
    }
    request(name, payload, buffers = undefined, cancel) {
        const id = `${this._instance_number}--${this._current_packet_counter++}`;
        return new Promise((rs, rj) => {
            let finished = () => { };
            const awaiter = (packet) => {
                if (packet === null) {
                    rj(new Error("Client closed."));
                    return;
                }
                finished();
                if (!!packet.buffers) {
                    packet.payload.buffers = packet.buffers;
                }
                if (packet.type == "failure") {
                    rj(packet.payload);
                }
                else {
                    rs(packet.payload);
                }
            };
            if (cancel !== undefined) {
                finished = cancel(() => {
                    this._requests.delete(id);
                    rj(new Error("Request timed out."));
                });
            }
            this._requests.set(id, awaiter);
            this.channel.send({
                id,
                type: name,
                payload,
                buffers
            });
        });
    }
    close() {
        this._closeSubscription();
        const awaiters = [...this._requests.values()];
        this._requests.clear();
        for (let awaiter of awaiters)
            awaiter(null);
    }
}
function timeout(time) {
    return (cancel) => {
        const id = setTimeout(() => cancel(), time);
        return () => clearTimeout(id);
    };
}
function race(other) {
    return (cancel) => {
        other.then(() => cancel(), () => cancel());
        return () => { };
    };
}


/***/ }),

/***/ "./lib/svelte-widget.js":
/*!******************************!*\
  !*** ./lib/svelte-widget.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SvelteWidgetView": () => (/* binding */ SvelteWidgetView),
/* harmony export */   "widgetFor": () => (/* binding */ widgetFor)
/* harmony export */ });
/* harmony import */ var _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
/* harmony import */ var _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__);

/**
 * Simple Wrapper-Type for Svelte Components.
 */
class SvelteWidgetView extends _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__.DOMWidgetView {
    constructor() {
        super(...arguments);
        this.component = null;
    }
    /**
     * Destroys a svelte component.
     */
    _destroyComponent() {
        if (this.component !== null) {
            this.component.$destroy();
            this.component = null;
        }
    }
    /**
     * Renders the svelte component.
     *
     * Svelte will subscribe to model changes it cares about by itself.
     */
    render() {
        this._destroyComponent();
        this.component = this.buildComponent();
    }
    /**
     * Unmounts a svelte component.
     */
    remove() {
        this._destroyComponent();
        return super.remove();
    }
}
/**
 * Creates a new class for a specific widget.
 */
function widgetFor(c) {
    return class SvelteWidgetImpl extends SvelteWidgetView {
        buildComponent() {
            return new c({
                target: this.el,
                props: { component: this.model }
            });
        }
    };
}


/***/ }),

/***/ "./lib/utils.js":
/*!**********************!*\
  !*** ./lib/utils.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "model_attribute": () => (/* binding */ model_attribute),
/* harmony export */   "debounce": () => (/* binding */ debounce)
/* harmony export */ });
/**
 * Creates a Svelte-Store out of a backbone model attribute.
 *
 * @param model The backbone model this to attach
 * @param name  The name of the attribute to watch.
 */
function model_attribute(model, name) {
    return {
        // Just set the value
        set(value) {
            model.set(name, value);
            model.save();
        },
        // Change the value.
        update(updater) {
            model.set(name, updater(model.get(name)));
        },
        // Subscribe to changes to the value.
        subscribe(subscriber) {
            // Create our own function instance to make sure
            // one can remove it again with the Unsubscriber.
            const cb = (_, value) => {
                subscriber(value);
            };
            model.on(`change:${name}`, cb);
            subscriber(model.get(name));
            return () => {
                model.off(`change:${name}`, cb);
            };
        }
    };
}
function debounce(time, parent) {
    let currentId = -1;
    return {
        set(value) {
            if (currentId != -1)
                clearTimeout(currentId);
            currentId = setTimeout(() => {
                currentId = -1;
                parent.set(value);
            }, time);
        },
        update(update) {
            parent.update(update);
        },
        subscribe(subscriber) {
            return parent.subscribe(subscriber);
        }
    };
}


/***/ }),

/***/ "./lib/widgets/audio/index.js":
/*!************************************!*\
  !*** ./lib/widgets/audio/index.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AudioPlaybackWidget": () => (/* binding */ AudioPlaybackWidget)
/* harmony export */ });
/* harmony import */ var _Widget_svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Widget.svelte */ "./lib/widgets/audio/Widget.svelte");
/* harmony import */ var _svelte_widget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../svelte-widget */ "./lib/svelte-widget.js");


const AudioPlaybackWidget = (0,_svelte_widget__WEBPACK_IMPORTED_MODULE_0__.widgetFor)(_Widget_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]);


/***/ }),

/***/ "./lib/widgets/audio/player.js":
/*!*************************************!*\
  !*** ./lib/widgets/audio/player.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AudioPlayer": () => (/* binding */ AudioPlayer)
/* harmony export */ });
const COMBINED_FRAMES = 24;
const SAMPLES_PER_VS_FRAME = 3072;
const SAMPLES_PER_REQUEST = COMBINED_FRAMES * SAMPLES_PER_VS_FRAME;
// How many seconds should be loaded before
// playback should resume.
const PREFETCH_SECONDS = 5;
// How many seconds can be buffered before we
// pause requesting new chunks every second.
const BUFFER_HIGH_MARK_SECONDS = 30;
// How many seconds should be left before we
// suspend the audio.
const BUFFER_LOW_MARK_SECONDS = 2;
function calculatePosition(sample) {
    const frame = Math.floor(sample / SAMPLES_PER_REQUEST);
    const offset = sample % SAMPLES_PER_REQUEST;
    return [frame, offset];
}
async function clock(tickTime, tick) {
    let skipped = 0;
    let shouldContinue = true;
    do {
        const start = new Date().valueOf();
        shouldContinue = await tick(skipped);
        const end = new Date().valueOf();
        const dT = end - start;
        if (dT < tickTime) {
            skipped = 0;
            if (tickTime - dT < 100)
                continue; // Increase stability by skipping timeout on short times.
            await new Promise(rs => setTimeout(rs, tickTime - dT));
        }
        else {
            skipped = Math.ceil(tickTime / dT);
        }
    } while (shouldContinue);
}
function microtask(func) {
    new Promise(rs => rs()).then(() => func());
}
class AudioPlayer {
    constructor(source) {
        this._paused = true;
        this._onpause = null;
        this.ontick = () => { };
        this.source = source;
    }
    get playable() {
        return this._onpause === null;
    }
    async play(startAt = 0) {
        if (!this._paused)
            return;
        if (this._onpause !== null)
            return;
        this._paused = false;
        // Ensure we have a full integer start at.
        startAt = Math.floor(startAt);
        // Make sure the metadata is loaded.
        await this.source.loadMetadata();
        // Create a new audio context and suspend it until we got the data we need.
        const ctx = new AudioContext();
        await ctx.suspend();
        // Register the neccessary callbacks.
        this._onpause = () => ctx.suspend();
        // Find out where the seeked position starts at.
        let [nextFrame, currentOffset] = calculatePosition(startAt);
        // Calculation for the UI.
        let currentSecond = 0;
        const startSecond = startAt / this.source.sample_rate;
        const maxLength = (this.source.samples - startAt) / this.source.sample_rate;
        // Schedule a callback to inform the UI of the new state.
        let lastCurrentTime = 0;
        clock(500, async () => {
            if (ctx.state !== "closed")
                lastCurrentTime = ctx.currentTime;
            const event = {
                currentTime: Math.min(lastCurrentTime, maxLength) + startSecond,
                bufferSecond: Math.min(currentSecond, maxLength) + startSecond,
                playing: !this._paused
            };
            microtask(() => {
                this.ontick(event);
            });
            return !this._paused;
        }).catch(console.error);
        let lastBuffers;
        if (SAMPLES_PER_REQUEST - currentOffset > this.source.sample_rate) {
            //   1. >1 second left at the sample to start:
            //      Make the offset negative to cause the initial buffer to
            //      take from beyond the start of b2 below.
            //
            //             <OFFSET>
            //      SECOND         |----------------|
            //      BUFFER |-----------------------------|:-----....
            //
            //      or before:
            lastBuffers = new Array(this.source.channels);
            lastBuffers.fill(new ArrayBuffer(SAMPLES_PER_REQUEST * 4));
            currentOffset *= -1;
        }
        else {
            //   2. <1 second left:
            //      Prefetch the buffer and set it as the last buffer.
            //                              <-- OFFSET -->
            //      SECOND                  |----------------|
            //      BUFFER |-----------------------------|:-----....
            await this.source.render(nextFrame, (_, __, buffers) => {
                lastBuffers = buffers;
                return false;
            });
            nextFrame++;
            currentOffset = SAMPLES_PER_REQUEST - currentOffset;
        }
        try {
            await clock(1000, async (skipped) => {
                if (this._paused)
                    return false;
                // If we finished rendering the node, play to the end.
                if (nextFrame >= this.source.frames) {
                    return currentSecond >= ctx.currentTime;
                }
                // Stop rendering after having buffered for 30 seconds and we did not skip any ticks.
                if (skipped == 0 && currentSecond - ctx.currentTime > BUFFER_HIGH_MARK_SECONDS)
                    return true;
                // All other cases: Process additional frames
                await this.source.render(nextFrame, (frameNo, _, buffers) => {
                    // Bail on pausing.
                    if (this._paused)
                        return false;
                    if (currentSecond - ctx.currentTime < BUFFER_LOW_MARK_SECONDS) {
                        ctx.suspend();
                    }
                    // Advance the frame counter.
                    nextFrame = frameNo + 1;
                    // Build the AudioBuffer instances that we can construct.
                    // All of them are for exactly one full second.
                    const result = buildBuffer(this.source, lastBuffers, buffers, currentOffset, this.source.sample_rate);
                    currentOffset = result[1];
                    lastBuffers = buffers;
                    // Queue the samples.
                    for (let audio of result[0]) {
                        const node = new AudioBufferSourceNode(ctx, { buffer: audio });
                        node.connect(ctx.destination);
                        node.start(currentSecond++);
                    }
                    // Stop fetching additional chunks if we step over prefetch.
                    return currentSecond - ctx.currentTime < PREFETCH_SECONDS;
                });
                if (ctx.state === "suspended" && !this._paused)
                    await ctx.resume();
                return !this._paused;
            });
        }
        finally {
            ctx.close();
            this._onpause = null;
            this._paused = true;
        }
    }
    pause() {
        if (!!this._onpause)
            this._onpause();
        this._paused = true;
    }
    async open() {
        this.source.open();
        await this.source.loadMetadata();
    }
}
function buildBuffer(source, buffer1, buffer2, offset, length) {
    const b1 = buffer1[0].byteLength / 4;
    const b2 = buffer2[0].byteLength / 4;
    const lb = length - offset;
    let rest = b2 - lb;
    const result = [];
    if (offset >= 0) {
        const buffer = new AudioBuffer({
            length,
            sampleRate: source.sample_rate,
            numberOfChannels: source.channels
        });
        result.push(buffer);
        if (offset > 0) {
            copyFromBuffers(buffer, buffer1, b1 - offset, 0);
        }
        copyFromBuffers(buffer, buffer2, 0, offset);
    }
    while (rest > length) {
        const buffer = new AudioBuffer({
            length,
            sampleRate: source.sample_rate,
            numberOfChannels: source.channels
        });
        result.push(buffer);
        copyFromBuffers(buffer, buffer2, b2 - rest, 0);
        rest -= length;
    }
    return [result, rest];
}
function copyFromBuffers(buffer, channels, channelOffset, startOffset) {
    for (let channel = 0; channel < channels.length; channel++) {
        buffer.copyToChannel(new Float32Array(channels[channel], channelOffset * 4), channel, startOffset);
    }
}


/***/ }),

/***/ "./lib/widgets/audio/rpc.js":
/*!**********************************!*\
  !*** ./lib/widgets/audio/rpc.js ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AudioSource": () => (/* binding */ AudioSource)
/* harmony export */ });
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../rpc */ "./lib/rpc.js");
/* harmony import */ var _model_rpc__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../model-rpc */ "./lib/model-rpc.js");


class AudioSource {
    constructor(model) {
        this._open = false;
        this._channels = 0;
        this._frames = 0;
        this._loaded = 0;
        this._samples = 0;
        this._sample_rate = 0;
        this.ondata = () => { };
        this.rpc = new _rpc__WEBPACK_IMPORTED_MODULE_0__.RPCClient(new _model_rpc__WEBPACK_IMPORTED_MODULE_1__.WidgetChannel(model)).makeProxy((0,_rpc__WEBPACK_IMPORTED_MODULE_0__.timeout)(10000));
    }
    open() {
        this.rpc.open();
        this._open = true;
    }
    close() {
        this._open = false;
        this.rpc.close();
    }
    get channels() {
        return this._channels;
    }
    get loaded() {
        return this._loaded;
    }
    get samples() {
        return this._samples;
    }
    get sample_rate() {
        return this._sample_rate;
    }
    get frames() {
        return this._frames;
    }
    get duration() {
        return this._samples / this._sample_rate;
    }
    async loadMetadata() {
        if (this._frames === 0) {
            const { frames, channel_count, samples_per_second, sample_count } = await this.rpc.meta();
            this._frames = frames;
            this._sample_rate = samples_per_second;
            this._samples = sample_count;
            this._channels = channel_count;
        }
        this.ondata();
    }
    async render(start, received) {
        if (this._frames === 0)
            await this.loadMetadata();
        for (let frame = start; frame < this._frames; frame++) {
            if (!this._open)
                break;
            const { size, buffers } = await this.rpc.render({ frame });
            this._loaded += size;
            if (!received(frame, size, buffers))
                break;
        }
    }
}


/***/ }),

/***/ "./lib/widgets/encode/index.js":
/*!*************************************!*\
  !*** ./lib/widgets/encode/index.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EncodeWindowWidget": () => (/* binding */ EncodeWindowWidget)
/* harmony export */ });
/* harmony import */ var _Widget_svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Widget.svelte */ "./lib/widgets/encode/Widget.svelte");
/* harmony import */ var _svelte_widget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../svelte-widget */ "./lib/svelte-widget.js");


const EncodeWindowWidget = (0,_svelte_widget__WEBPACK_IMPORTED_MODULE_0__.widgetFor)(_Widget_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]);


/***/ }),

/***/ "./lib/widgets/encode/rpc.js":
/*!***********************************!*\
  !*** ./lib/widgets/encode/rpc.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "getRPCForModel": () => (/* binding */ getRPCForModel)
/* harmony export */ });
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../rpc */ "./lib/rpc.js");
/* harmony import */ var _model_rpc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../model-rpc */ "./lib/model-rpc.js");


function getRPCForModel(model) {
    const channel = new _model_rpc__WEBPACK_IMPORTED_MODULE_0__.WidgetChannel(model);
    return new _rpc__WEBPACK_IMPORTED_MODULE_1__.RPCClient(channel).makeProxy((0,_rpc__WEBPACK_IMPORTED_MODULE_1__.timeout)(10000));
}


/***/ }),

/***/ "./lib/widgets/preview/index.js":
/*!**************************************!*\
  !*** ./lib/widgets/preview/index.js ***!
  \**************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "PreviewWindowWidget": () => (/* binding */ PreviewWindowWidget)
/* harmony export */ });
/* harmony import */ var _Widget_svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Widget.svelte */ "./lib/widgets/preview/Widget.svelte");
/* harmony import */ var _svelte_widget__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../svelte-widget */ "./lib/svelte-widget.js");


const PreviewWindowWidget = (0,_svelte_widget__WEBPACK_IMPORTED_MODULE_0__.widgetFor)(_Widget_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]);


/***/ }),

/***/ "./lib/widgets/preview/rpc.js":
/*!************************************!*\
  !*** ./lib/widgets/preview/rpc.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "getRPCForModel": () => (/* binding */ getRPCForModel)
/* harmony export */ });
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../rpc */ "./lib/rpc.js");
/* harmony import */ var _model_rpc__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ../../model-rpc */ "./lib/model-rpc.js");


class CachedPreviewRPC {
    constructor(parent, model) {
        this._cache = new Map();
        this._lru = [];
        this.parent = parent;
        this.model = model;
    }
    clear() {
        this._cache.clear();
    }
    open() {
        this.parent.open();
    }
    close() {
        this.parent.close();
    }
    length() {
        return this.parent.length();
    }
    frame({ frame, image }) {
        if (!image)
            image = "clip";
        const _lru_id = `${this.model.get(image + "Id")}--${image}--${frame}`;
        if (!this._cache.has(_lru_id)) {
            this._evict();
            this._cache.set(_lru_id, this.parent.frame({ frame, image }));
        }
        this._hit(_lru_id);
        return this._cache.get(_lru_id);
    }
    _hit(id) {
        if (this._lru.indexOf(id) == 0)
            return;
        this._lru = [id, ...this._lru.filter(f => f != id)];
    }
    _evict() {
        if (this._lru.length <= 10)
            return;
        const evicted = this._lru.pop();
        this._cache.delete(evicted);
    }
}
function getRPCForModel(model) {
    const channel = new _model_rpc__WEBPACK_IMPORTED_MODULE_0__.WidgetChannel(model);
    return new CachedPreviewRPC(new _rpc__WEBPACK_IMPORTED_MODULE_1__.RPCClient(channel).makeProxy((0,_rpc__WEBPACK_IMPORTED_MODULE_1__.timeout)(10000)), model);
}


/***/ }),

/***/ "./lib/widgets/audio/BufferSlider.svelte":
/*!***********************************************!*\
  !*** ./lib/widgets/audio/BufferSlider.svelte ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* lib/widgets/audio/BufferSlider.svelte generated by Svelte v3.44.3 */




function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1035j7a", ".buffer-slider.svelte-1035j7a.svelte-1035j7a{position:relative;width:100%;height:100%;display:block;border-left:var(--jp-border-width) solid var(--jp-cell-editor-border-color);border-right:var(--jp-border-width) solid var(--jp-cell-editor-border-color)}.buffer-slider.svelte-1035j7a>.svelte-1035j7a{position:absolute;height:20%;bottom:40%}.past.svelte-1035j7a.svelte-1035j7a{left:0;background-color:var(--jp-brand-color1);z-index:1}.buffered.svelte-1035j7a.svelte-1035j7a{left:0;background-color:var(--jp-cell-editor-border-color)}.select.svelte-1035j7a.svelte-1035j7a,.proposed.svelte-1035j7a.svelte-1035j7a{height:100%;top:0;width:var(--jp-border-width);background-color:var(--jp-brand-color1);z-index:2}");
}

// (5:4) {:else}
function create_else_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "proposed svelte-1035j7a");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*proposedPerc*/ ctx[1] * 100 + "%");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p(ctx, dirty) {
			if (dirty & /*proposedPerc*/ 2) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*proposedPerc*/ ctx[1] * 100 + "%");
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (3:4) {#if proposedValue === null}
function create_if_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "select svelte-1035j7a");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*percPast*/ ctx[4] * 100 + "%");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p(ctx, dirty) {
			if (dirty & /*percPast*/ 16) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*percPast*/ ctx[4] * 100 + "%");
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

function create_fragment(ctx) {
	let div2;
	let div0;
	let t0;
	let t1;
	let div1;
	let mounted;
	let dispose;

	function select_block_type(ctx, dirty) {
		if (/*proposedValue*/ ctx[0] === null) return create_if_block;
		return create_else_block;
	}

	let current_block_type = select_block_type(ctx, -1);
	let if_block = current_block_type(ctx);

	return {
		c() {
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			if_block.c();
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "past svelte-1035j7a");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div0, "width", /*percPast*/ ctx[4] * 100 + "%");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "buffered svelte-1035j7a");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div1, "width", /*percFuture*/ ctx[3] * 100 + "%");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "buffer-slider svelte-1035j7a");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, div0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, t0);
			if_block.m(div2, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, div1);
			/*div2_binding*/ ctx[14](div2);

			if (!mounted) {
				dispose = [
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "mouseenter", /*enter*/ ctx[5]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "mouseleave", /*leave*/ ctx[6]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "mousemove", /*move*/ ctx[7]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "click", /*submit*/ ctx[8])
				];

				mounted = true;
			}
		},
		p(ctx, [dirty]) {
			if (dirty & /*percPast*/ 16) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div0, "width", /*percPast*/ ctx[4] * 100 + "%");
			}

			if (current_block_type === (current_block_type = select_block_type(ctx, dirty)) && if_block) {
				if_block.p(ctx, dirty);
			} else {
				if_block.d(1);
				if_block = current_block_type(ctx);

				if (if_block) {
					if_block.c();
					if_block.m(div2, t1);
				}
			}

			if (dirty & /*percFuture*/ 8) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div1, "width", /*percFuture*/ ctx[3] * 100 + "%");
			}
		},
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div2);
			if_block.d();
			/*div2_binding*/ ctx[14](null);
			mounted = false;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.run_all)(dispose);
		}
	};
}

function clamp(v, ma, mi) {
	return Math.max(Math.min(v, ma), mi);
}

function instance($$self, $$props, $$invalidate) {
	let span;
	let percPast;
	let percFuture;
	let { value = 0 } = $$props;
	let { max = 1 } = $$props;
	let { min = 0 } = $$props;
	let { buffered = 0 } = $$props;
	let { proposedValue = null } = $$props;
	let { proposedPerc = null } = $$props;
	const dispatch = (0,svelte__WEBPACK_IMPORTED_MODULE_1__.createEventDispatcher)();
	let myself;

	function enter(event) {
		$$invalidate(0, proposedValue = min);
		move(event);
	}

	function leave() {
		$$invalidate(0, proposedValue = null);
	}

	function move(event) {
		const { pageX, pageY } = event;
		const { left, top, right } = myself.getBoundingClientRect();
		const width = right - left;
		const vX = pageX - left;
		$$invalidate(1, proposedPerc = vX / width);
		const rawProposal = proposedPerc * span + min;
		$$invalidate(0, proposedValue = Math.round(rawProposal));
	}

	function submit() {
		dispatch('update', { old: value, new: proposedValue });
		$$invalidate(9, value = proposedValue);
	}

	function div2_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			myself = $$value;
			$$invalidate(2, myself);
		});
	}

	$$self.$$set = $$props => {
		if ('value' in $$props) $$invalidate(9, value = $$props.value);
		if ('max' in $$props) $$invalidate(10, max = $$props.max);
		if ('min' in $$props) $$invalidate(11, min = $$props.min);
		if ('buffered' in $$props) $$invalidate(12, buffered = $$props.buffered);
		if ('proposedValue' in $$props) $$invalidate(0, proposedValue = $$props.proposedValue);
		if ('proposedPerc' in $$props) $$invalidate(1, proposedPerc = $$props.proposedPerc);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*max, min*/ 3072) {
			$: $$invalidate(13, span = max - min);
		}

		if ($$self.$$.dirty & /*value, min, span*/ 10752) {
			$: $$invalidate(4, percPast = clamp((value - min) / span, 1, 0));
		}

		if ($$self.$$.dirty & /*buffered, min, span*/ 14336) {
			$: $$invalidate(3, percFuture = clamp((buffered - min) / span, 1, 0));
		}
	};

	return [
		proposedValue,
		proposedPerc,
		myself,
		percFuture,
		percPast,
		enter,
		leave,
		move,
		submit,
		value,
		max,
		min,
		buffered,
		span,
		div2_binding
	];
}

class BufferSlider extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();

		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(
			this,
			options,
			instance,
			create_fragment,
			svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal,
			{
				value: 9,
				max: 10,
				min: 11,
				buffered: 12,
				proposedValue: 0,
				proposedPerc: 1
			},
			add_css
		);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (BufferSlider);

/***/ }),

/***/ "./lib/widgets/audio/Widget.svelte":
/*!*****************************************!*\
  !*** ./lib/widgets/audio/Widget.svelte ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _BufferSlider_svelte__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./BufferSlider.svelte */ "./lib/widgets/audio/BufferSlider.svelte");
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./rpc */ "./lib/widgets/audio/rpc.js");
/* harmony import */ var _player__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./player */ "./lib/widgets/audio/player.js");
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* lib/widgets/audio/Widget.svelte generated by Svelte v3.44.3 */








function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-62r26p", ".audio.svelte-62r26p.svelte-62r26p{border:var(--jp-border-width) solid var(--jp-cell-editor-border-color);border-radius:0px;background:var(--jp-cell-editor-background);display:flex;height:28px}.audio.svelte-62r26p>.svelte-62r26p{padding:0px 10px}.audio.svelte-62r26p>.svelte-62r26p:not(:last-child){border-right:var(--jp-border-width) solid var(--jp-cell-editor-border-color)}.audio.svelte-62r26p>.meta.svelte-62r26p{line-height:28px}.audio.svelte-62r26p>.slider.svelte-62r26p{padding:0;flex-grow:1;flex-shrink:1}.toolbar.svelte-62r26p.svelte-62r26p{border:0;background:transparent;margin:0;padding:0;line-height:35px}.toolbar.svelte-62r26p.svelte-62r26p:not(:last-child){padding-right:5px}");
}

// (11:8) {:else}
function create_else_block(ctx) {
	let button;
	let mounted;
	let dispose;

	return {
		c() {
			button = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button, "class", "toolbar svelte-62r26p");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, button, anchor);
			/*button_binding_1*/ ctx[25](button);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button, "click", /*click_handler_1*/ ctx[24]);
				mounted = true;
			}
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(button);
			/*button_binding_1*/ ctx[25](null);
			mounted = false;
			dispose();
		}
	};
}

// (9:8) {#if playing}
function create_if_block(ctx) {
	let button;
	let mounted;
	let dispose;

	return {
		c() {
			button = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button, "class", "toolbar svelte-62r26p");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, button, anchor);
			/*button_binding*/ ctx[23](button);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button, "click", /*click_handler*/ ctx[22]);
				mounted = true;
			}
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(button);
			/*button_binding*/ ctx[23](null);
			mounted = false;
			dispose();
		}
	};
}

function create_fragment(ctx) {
	let div3;
	let div0;
	let t0;
	let t1;
	let div1;
	let bufferslider;
	let updating_value;
	let updating_proposedValue;
	let t2;
	let div2;
	let t3;
	let button;
	let current;
	let mounted;
	let dispose;

	function bufferslider_value_binding(value) {
		/*bufferslider_value_binding*/ ctx[20](value);
	}

	function bufferslider_proposedValue_binding(value) {
		/*bufferslider_proposedValue_binding*/ ctx[21](value);
	}

	let bufferslider_props = {
		buffered: /*loaded*/ ctx[3],
		samples: /*samples*/ ctx[2],
		max: /*sample_count*/ ctx[8]
	};

	if (/*playhead*/ ctx[0] !== void 0) {
		bufferslider_props.value = /*playhead*/ ctx[0];
	}

	if (/*proposed*/ ctx[1] !== void 0) {
		bufferslider_props.proposedValue = /*proposed*/ ctx[1];
	}

	bufferslider = new _BufferSlider_svelte__WEBPACK_IMPORTED_MODULE_3__["default"]({ props: bufferslider_props });
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(bufferslider, 'value', bufferslider_value_binding));
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(bufferslider, 'proposedValue', bufferslider_proposedValue_binding));
	bufferslider.$on("update", /*seek*/ ctx[11]);

	function select_block_type(ctx, dirty) {
		if (/*playing*/ ctx[9]) return create_if_block;
		return create_else_block;
	}

	let current_block_type = select_block_type(ctx, [-1, -1]);
	let if_block = current_block_type(ctx);

	return {
		c() {
			div3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(/*displayTime*/ ctx[10]);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(bufferslider.$$.fragment);
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			if_block.c();
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			button = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "meta svelte-62r26p");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "slider svelte-62r26p");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button, "class", "toolbar svelte-62r26p");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", " svelte-62r26p");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div3, "class", "audio svelte-62r26p");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div3, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div0, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(bufferslider, div1, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div2);
			if_block.m(div2, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, t3);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, button);
			/*button_binding_2*/ ctx[27](button);
			current = true;

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button, "click", /*click_handler_2*/ ctx[26]);
				mounted = true;
			}
		},
		p(ctx, dirty) {
			if (!current || dirty[0] & /*displayTime*/ 1024) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t0, /*displayTime*/ ctx[10]);
			const bufferslider_changes = {};
			if (dirty[0] & /*loaded*/ 8) bufferslider_changes.buffered = /*loaded*/ ctx[3];
			if (dirty[0] & /*samples*/ 4) bufferslider_changes.samples = /*samples*/ ctx[2];
			if (dirty[0] & /*sample_count*/ 256) bufferslider_changes.max = /*sample_count*/ ctx[8];

			if (!updating_value && dirty[0] & /*playhead*/ 1) {
				updating_value = true;
				bufferslider_changes.value = /*playhead*/ ctx[0];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_value = false);
			}

			if (!updating_proposedValue && dirty[0] & /*proposed*/ 2) {
				updating_proposedValue = true;
				bufferslider_changes.proposedValue = /*proposed*/ ctx[1];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_proposedValue = false);
			}

			bufferslider.$set(bufferslider_changes);

			if (current_block_type === (current_block_type = select_block_type(ctx, dirty)) && if_block) {
				if_block.p(ctx, dirty);
			} else {
				if_block.d(1);
				if_block = current_block_type(ctx);

				if (if_block) {
					if_block.c();
					if_block.m(div2, t3);
				}
			}
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(bufferslider.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(bufferslider.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div3);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(bufferslider);
			if_block.d();
			/*button_binding_2*/ ctx[27](null);
			mounted = false;
			dispose();
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let percBuffered;
	let displaySamples;
	let raw_seconds;
	let seconds;
	let minutes;
	let hours;
	let displayTimeMinutes;
	let displayTime;
	let { component } = $$props;
	let myself;
	const audioSource = new _rpc__WEBPACK_IMPORTED_MODULE_4__.AudioSource(component);
	const player = new _player__WEBPACK_IMPORTED_MODULE_5__.AudioPlayer(audioSource);
	let playhead = 0;
	let proposed = null;
	let sample_count = 0;
	let sample_rate = 0;
	let samples = 1;
	let loaded = 0;
	let seeking = false;
	let playing = false;

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onMount)(async () => {
		audioSource.open();
		audioSource.loadMetadata();

		audioSource.ondata = () => {
			$$invalidate(8, sample_count = audioSource.samples);
			$$invalidate(13, sample_rate = audioSource.sample_rate);
			$$invalidate(2, samples = audioSource.samples);
		};

		$$invalidate(
			7,
			player.ontick = event => {
				if (seeking) return;
				$$invalidate(9, playing = event.playing);
				$$invalidate(0, playhead = event.currentTime * audioSource.sample_rate);
				$$invalidate(3, loaded = event.bufferSecond * audioSource.sample_rate);
			},
			player
		);
	});

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onDestroy)(() => {
		audioSource.close();
		player.pause();
	});

	async function seek(event) {
		// Run as expected if we are not playing back.
		if (!playing) return;

		// Pause and restart at the desired position.
		seeking = true;

		player.pause();

		while (!player.playable) {
			await new Promise(rs => setTimeout(rs, 1));
		}

		seeking = false;
		player.play(event.detail.new);
	}

	let playBtn, pauseBtn, stopBtn;

	function bufferslider_value_binding(value) {
		playhead = value;
		$$invalidate(0, playhead);
	}

	function bufferslider_proposedValue_binding(value) {
		proposed = value;
		$$invalidate(1, proposed);
	}

	const click_handler = () => {
		player.pause();
	};

	function button_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			pauseBtn = $$value;
			$$invalidate(5, pauseBtn);
		});
	}

	const click_handler_1 = () => {
		player.play(playhead);
	};

	function button_binding_1($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			playBtn = $$value;
			$$invalidate(4, playBtn);
		});
	}

	const click_handler_2 = () => {
		player.pause();
		$$invalidate(0, playhead = 0);
	};

	function button_binding_2($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			stopBtn = $$value;
			$$invalidate(6, stopBtn);
		});
	}

	$$self.$$set = $$props => {
		if ('component' in $$props) $$invalidate(12, component = $$props.component);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty[0] & /*samples, loaded*/ 12) {
			$: percBuffered = samples / loaded;
		}

		if ($$self.$$.dirty[0] & /*proposed, playhead*/ 3) {
			$: $$invalidate(19, displaySamples = proposed === null ? playhead : proposed);
		}

		if ($$self.$$.dirty[0] & /*displaySamples, sample_rate*/ 532480) {
			$: $$invalidate(18, raw_seconds = Math.round(displaySamples / sample_rate));
		}

		if ($$self.$$.dirty[0] & /*raw_seconds*/ 262144) {
			$: $$invalidate(16, seconds = raw_seconds % 60);
		}

		if ($$self.$$.dirty[0] & /*raw_seconds*/ 262144) {
			$: $$invalidate(17, minutes = Math.floor(raw_seconds / 60) % 60);
		}

		if ($$self.$$.dirty[0] & /*raw_seconds*/ 262144) {
			$: $$invalidate(15, hours = Math.floor(raw_seconds / 3600));
		}

		if ($$self.$$.dirty[0] & /*minutes, seconds*/ 196608) {
			$: $$invalidate(14, displayTimeMinutes = `${(minutes + "").padStart(2, "0")}:${(seconds + "").padStart(2, "0")}`);
		}

		if ($$self.$$.dirty[0] & /*hours, displayTimeMinutes*/ 49152) {
			$: $$invalidate(10, displayTime = hours < 1
			? displayTimeMinutes
			: `${hours}:${displayTimeMinutes}`);
		}

		if ($$self.$$.dirty[0] & /*stopBtn*/ 64) {
			$: if (!!stopBtn) _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.refreshIcon.element({
				container: stopBtn,
				width: '16px',
				height: '16px',
				marginLeft: '2px'
			});
		}

		if ($$self.$$.dirty[0] & /*playBtn*/ 16) {
			$: if (!!playBtn) _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.runIcon.element({
				container: playBtn,
				width: '16px',
				height: '16px',
				marginLeft: '2px'
			});
		}

		if ($$self.$$.dirty[0] & /*pauseBtn*/ 32) {
			$: if (!!pauseBtn) _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.stopIcon.element({
				container: pauseBtn,
				width: '16px',
				height: '16px',
				marginLeft: '2px'
			});
		}
	};

	return [
		playhead,
		proposed,
		samples,
		loaded,
		playBtn,
		pauseBtn,
		stopBtn,
		player,
		sample_count,
		playing,
		displayTime,
		seek,
		component,
		sample_rate,
		displayTimeMinutes,
		hours,
		seconds,
		minutes,
		raw_seconds,
		displaySamples,
		bufferslider_value_binding,
		bufferslider_proposedValue_binding,
		click_handler,
		button_binding,
		click_handler_1,
		button_binding_1,
		click_handler_2,
		button_binding_2
	];
}

class Widget extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { component: 12 }, add_css, [-1, -1]);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Widget);

/***/ }),

/***/ "./lib/widgets/encode/Clock.svelte":
/*!*****************************************!*\
  !*** ./lib/widgets/encode/Clock.svelte ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* lib/widgets/encode/Clock.svelte generated by Svelte v3.44.3 */




function create_fragment(ctx) {
	let span;
	let t;

	return {
		c() {
			span = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("span");
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(/*running_time*/ ctx[0]);
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, span, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(span, t);
		},
		p(ctx, [dirty]) {
			if (dirty & /*running_time*/ 1) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t, /*running_time*/ ctx[0]);
		},
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(span);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let current_time;
	let dTime;
	let seconds;
	let minutes;
	let hours;
	let days;
	let intra_day;
	let running_time;
	let { end_time } = $$props;
	let { start_time } = $$props;
	let { terminated } = $$props;
	let clock = new Date().valueOf();

	let interval = setInterval(
		() => {
			$$invalidate(4, clock = new Date().valueOf());
		},
		1000
	);

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onDestroy)(() => {
		clearInterval(interval);
	});

	$$self.$$set = $$props => {
		if ('end_time' in $$props) $$invalidate(1, end_time = $$props.end_time);
		if ('start_time' in $$props) $$invalidate(2, start_time = $$props.start_time);
		if ('terminated' in $$props) $$invalidate(3, terminated = $$props.terminated);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*terminated, end_time, clock*/ 26) {
			$: $$invalidate(11, current_time = terminated ? end_time : Math.round(clock / 1000));
		}

		if ($$self.$$.dirty & /*current_time, start_time*/ 2052) {
			$: $$invalidate(10, dTime = current_time - start_time);
		}

		if ($$self.$$.dirty & /*dTime*/ 1024) {
			$: $$invalidate(8, seconds = dTime % 60);
		}

		if ($$self.$$.dirty & /*dTime*/ 1024) {
			$: $$invalidate(9, minutes = Math.round(dTime / 60) % 60);
		}

		if ($$self.$$.dirty & /*dTime*/ 1024) {
			$: $$invalidate(6, hours = Math.round(dTime / 3600) % 24);
		}

		if ($$self.$$.dirty & /*dTime*/ 1024) {
			$: $$invalidate(7, days = Math.round(dTime / 86400));
		}

		if ($$self.$$.dirty & /*minutes, seconds*/ 768) {
			$: $$invalidate(5, intra_day = `${(minutes + "").padStart(2, "0")}:${(seconds + "").padStart(2, "0")}`);
		}

		if ($$self.$$.dirty & /*days, hours, intra_day*/ 224) {
			$: $$invalidate(0, running_time = days > 0
			? `${days + ""}:${(hours + "").padStart(2, "0")}:${intra_day}`
			: `${hours + ""}:${intra_day}`);
		}
	};

	return [
		running_time,
		end_time,
		start_time,
		terminated,
		clock,
		intra_day,
		hours,
		days,
		seconds,
		minutes,
		dTime,
		current_time
	];
}

class Clock extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();

		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, {
			end_time: 1,
			start_time: 2,
			terminated: 3
		});
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Clock);

/***/ }),

/***/ "./lib/widgets/encode/Header.svelte":
/*!******************************************!*\
  !*** ./lib/widgets/encode/Header.svelte ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _Progress_svelte__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./Progress.svelte */ "./lib/widgets/encode/Progress.svelte");
/* harmony import */ var _Clock_svelte__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./Clock.svelte */ "./lib/widgets/encode/Clock.svelte");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../utils */ "./lib/utils.js");
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./rpc */ "./lib/widgets/encode/rpc.js");
/* lib/widgets/encode/Header.svelte generated by Svelte v3.44.3 */








function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-14bawlj", ".header.svelte-14bawlj.svelte-14bawlj{width:100%}.top-bg.svelte-14bawlj.svelte-14bawlj{width:100%;top:0;left:0}.top.svelte-14bawlj.svelte-14bawlj{display:flex;line-height:27px;height:27px}.top.svelte-14bawlj>.svelte-14bawlj{padding:0px 10px}.top.svelte-14bawlj>.svelte-14bawlj:not(:last-child){border-right:var(--jp-border-width) solid var(--jp-cell-editor-border-color)}.spacer.svelte-14bawlj.svelte-14bawlj{flex-grow:1;flex-shrink:1}.toolbar.svelte-14bawlj.svelte-14bawlj{border:0;background:transparent;margin:0;padding:0;line-height:35px}.toolbar.svelte-14bawlj.svelte-14bawlj:not(:last-child){padding-right:5px}");
}

// (13:8) {:else}
function create_else_block(ctx) {
	let div;
	let t;
	let button;
	let mounted;
	let dispose;
	let if_block = !/*$_w32*/ ctx[9] && create_if_block_1(ctx);

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			if (if_block) if_block.c();
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			button = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button, "class", "toolbar svelte-14bawlj");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-14bawlj");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			if (if_block) if_block.m(div, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, button);
			/*button_binding_1*/ ctx[21](button);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button, "click", /*click_handler_1*/ ctx[20]);
				mounted = true;
			}
		},
		p(ctx, dirty) {
			if (!/*$_w32*/ ctx[9]) {
				if (if_block) {
					if_block.p(ctx, dirty);
				} else {
					if_block = create_if_block_1(ctx);
					if_block.c();
					if_block.m(div, t);
				}
			} else if (if_block) {
				if_block.d(1);
				if_block = null;
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
			if (if_block) if_block.d();
			/*button_binding_1*/ ctx[21](null);
			mounted = false;
			dispose();
		}
	};
}

// (11:8) {#if $terminated}
function create_if_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Terminated";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-14bawlj");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (15:16) {#if !$_w32}
function create_if_block_1(ctx) {
	let button;
	let mounted;
	let dispose;

	return {
		c() {
			button = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button, "class", "toolbar svelte-14bawlj");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, button, anchor);
			/*button_binding*/ ctx[19](button);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button, "click", /*click_handler*/ ctx[18]);
				mounted = true;
			}
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(button);
			/*button_binding*/ ctx[19](null);
			mounted = false;
			dispose();
		}
	};
}

function create_fragment(ctx) {
	let div5;
	let div0;
	let progress;
	let t0;
	let div4;
	let div1;
	let t1;
	let t2;
	let t3;
	let t4;
	let div2;
	let clock;
	let t5;
	let div3;
	let t6;
	let t7;
	let current;

	progress = new _Progress_svelte__WEBPACK_IMPORTED_MODULE_2__["default"]({
			props: {
				min: 0,
				max: /*$length*/ ctx[3],
				value: /*$current*/ ctx[4]
			}
		});

	clock = new _Clock_svelte__WEBPACK_IMPORTED_MODULE_3__["default"]({
			props: {
				start_time: /*$start_time*/ ctx[5],
				end_time: /*$end_time*/ ctx[6],
				terminated: /*$terminated*/ ctx[7]
			}
		});

	function select_block_type(ctx, dirty) {
		if (/*$terminated*/ ctx[7]) return create_if_block;
		return create_else_block;
	}

	let current_block_type = select_block_type(ctx, -1);
	let if_block = current_block_type(ctx);

	return {
		c() {
			div5 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(progress.$$.fragment);
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div4 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(/*$current*/ ctx[4]);
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(" / ");
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(/*$length*/ ctx[3]);
			t4 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(clock.$$.fragment);
			t5 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t6 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(/*$commandline*/ ctx[8]);
			t7 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			if_block.c();
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "top-bg svelte-14bawlj");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "svelte-14bawlj");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "svelte-14bawlj");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div3, "class", "spacer svelte-14bawlj");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div4, "class", "top svelte-14bawlj");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div5, "class", "header svelte-14bawlj");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div5, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div5, div0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(progress, div0, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div5, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div5, div4);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div4, div1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div1, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div1, t2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div1, t3);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div4, t4);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div4, div2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(clock, div2, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div4, t5);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div4, div3);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t6);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div4, t7);
			if_block.m(div4, null);
			current = true;
		},
		p(ctx, [dirty]) {
			const progress_changes = {};
			if (dirty & /*$length*/ 8) progress_changes.max = /*$length*/ ctx[3];
			if (dirty & /*$current*/ 16) progress_changes.value = /*$current*/ ctx[4];
			progress.$set(progress_changes);
			if (!current || dirty & /*$current*/ 16) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t1, /*$current*/ ctx[4]);
			if (!current || dirty & /*$length*/ 8) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t3, /*$length*/ ctx[3]);
			const clock_changes = {};
			if (dirty & /*$start_time*/ 32) clock_changes.start_time = /*$start_time*/ ctx[5];
			if (dirty & /*$end_time*/ 64) clock_changes.end_time = /*$end_time*/ ctx[6];
			if (dirty & /*$terminated*/ 128) clock_changes.terminated = /*$terminated*/ ctx[7];
			clock.$set(clock_changes);
			if (!current || dirty & /*$commandline*/ 256) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t6, /*$commandline*/ ctx[8]);

			if (current_block_type === (current_block_type = select_block_type(ctx, dirty)) && if_block) {
				if_block.p(ctx, dirty);
			} else {
				if_block.d(1);
				if_block = current_block_type(ctx);

				if (if_block) {
					if_block.c();
					if_block.m(div4, null);
				}
			}
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(progress.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(clock.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(progress.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(clock.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div5);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(progress);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(clock);
			if_block.d();
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let rpc;
	let $length;
	let $current;
	let $start_time;
	let $end_time;
	let $terminated;
	let $commandline;
	let $_w32;
	let { component } = $$props;
	let interruptBtn, stopBtn;
	const commandline = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "commandline");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, commandline, value => $$invalidate(8, $commandline = value));
	const current = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "current");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, current, value => $$invalidate(4, $current = value));
	const length = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "length");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, length, value => $$invalidate(3, $length = value));
	const terminated = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "terminated");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, terminated, value => $$invalidate(7, $terminated = value));
	const start_time = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "start_time");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, start_time, value => $$invalidate(5, $start_time = value));
	const end_time = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "end_time");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, end_time, value => $$invalidate(6, $end_time = value));
	const _w32 = (0,_utils__WEBPACK_IMPORTED_MODULE_4__.model_attribute)(component, "_w32");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, _w32, value => $$invalidate(9, $_w32 = value));

	const click_handler = () => {
		rpc.interrupt();
	};

	function button_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			interruptBtn = $$value;
			$$invalidate(0, interruptBtn);
		});
	}

	const click_handler_1 = () => {
		rpc.kill();
	};

	function button_binding_1($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			stopBtn = $$value;
			$$invalidate(1, stopBtn);
		});
	}

	$$self.$$set = $$props => {
		if ('component' in $$props) $$invalidate(17, component = $$props.component);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*component*/ 131072) {
			$: $$invalidate(2, rpc = (0,_rpc__WEBPACK_IMPORTED_MODULE_5__.getRPCForModel)(component));
		}

		if ($$self.$$.dirty & /*interruptBtn*/ 1) {
			$: [interruptBtn].forEach(e => {
				if (!!e) _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.closeIcon.element({
					container: e,
					width: '16px',
					height: '16px',
					marginLeft: '2px'
				});
			});
		}

		if ($$self.$$.dirty & /*stopBtn*/ 2) {
			$: [stopBtn].forEach(e => {
				if (!!e) _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.stopIcon.element({
					container: e,
					width: '16px',
					height: '16px',
					marginLeft: '2px'
				});
			});
		}
	};

	return [
		interruptBtn,
		stopBtn,
		rpc,
		$length,
		$current,
		$start_time,
		$end_time,
		$terminated,
		$commandline,
		$_w32,
		commandline,
		current,
		length,
		terminated,
		start_time,
		end_time,
		_w32,
		component,
		click_handler,
		button_binding,
		click_handler_1,
		button_binding_1
	];
}

class Header extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { component: 17 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Header);

/***/ }),

/***/ "./lib/widgets/encode/Progress.svelte":
/*!********************************************!*\
  !*** ./lib/widgets/encode/Progress.svelte ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* lib/widgets/encode/Progress.svelte generated by Svelte v3.44.3 */


function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1f3ta7d", ".progress.svelte-1f3ta7d.svelte-1f3ta7d{display:block;border-left:var(--jp-border-width) solid var(--jp-cell-editor-border-color);border-right:var(--jp-border-width) solid var(--jp-cell-editor-border-color)}.progress.svelte-1f3ta7d>.svelte-1f3ta7d{position:absolute;height:2px;top:0}.past.svelte-1f3ta7d.svelte-1f3ta7d{left:0;background-color:var(--jp-brand-color1)}");
}

function create_fragment(ctx) {
	let div1;
	let div0;

	return {
		c() {
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "past svelte-1f3ta7d");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div0, "width", /*percPast*/ ctx[0] * 100 + "%");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "progress svelte-1f3ta7d");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div1, div0);
		},
		p(ctx, [dirty]) {
			if (dirty & /*percPast*/ 1) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div0, "width", /*percPast*/ ctx[0] * 100 + "%");
			}
		},
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div1);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let span;
	let percPast;
	let { value = 0 } = $$props;
	let { max = 100 } = $$props;
	let { min = 0 } = $$props;

	$$self.$$set = $$props => {
		if ('value' in $$props) $$invalidate(1, value = $$props.value);
		if ('max' in $$props) $$invalidate(2, max = $$props.max);
		if ('min' in $$props) $$invalidate(3, min = $$props.min);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*max, min*/ 12) {
			$: $$invalidate(4, span = max - min);
		}

		if ($$self.$$.dirty & /*value, min, span*/ 26) {
			$: $$invalidate(0, percPast = (value - min) / span);
		}
	};

	return [percPast, value, max, min, span];
}

class Progress extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { value: 1, max: 2, min: 3 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Progress);

/***/ }),

/***/ "./lib/widgets/encode/Terminal.svelte":
/*!********************************************!*\
  !*** ./lib/widgets/encode/Terminal.svelte ***!
  \********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* harmony import */ var xterm__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! xterm */ "webpack/sharing/consume/default/xterm/xterm");
/* harmony import */ var xterm__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(xterm__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var xterm_addon_fit__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! xterm-addon-fit */ "webpack/sharing/consume/default/xterm-addon-fit/xterm-addon-fit");
/* harmony import */ var xterm_addon_fit__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(xterm_addon_fit__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./rpc */ "./lib/widgets/encode/rpc.js");
/* lib/widgets/encode/Terminal.svelte generated by Svelte v3.44.3 */







function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1kwq8fs", ".terminal.svelte-1kwq8fs{width:100%;min-height:480px\n    }");
}

function create_fragment(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "terminal svelte-1kwq8fs");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			/*div_binding*/ ctx[2](div);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
			/*div_binding*/ ctx[2](null);
		}
	};
}

let self_id = 0;

function instance($$self, $$props, $$invalidate) {
	let { component } = $$props;
	const myOwnId = `terminal-${self_id}`;
	let target;
	let state = "attaching";
	const terminal = new xterm__WEBPACK_IMPORTED_MODULE_2__.Terminal();
	const fit = new xterm_addon_fit__WEBPACK_IMPORTED_MODULE_3__.FitAddon();
	terminal.loadAddon(fit);
	const rpc = (0,_rpc__WEBPACK_IMPORTED_MODULE_4__.getRPCForModel)(component);

	const cb = msg => {
		if (msg.type !== "write") return;
		if (state !== "ready") return;
		if (msg.target !== "broadcast") return;
		terminal.write(msg.data);
	};

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onMount)(async () => {
		rpc.open();
		component.on("msg:custom", cb);
		terminal.write((await rpc.refresh({ source: myOwnId })).data);
		state = "ready";
	});

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onMount)(async () => {
		// Let's do our best to enforce style calculations.
		await new Promise(rs => requestAnimationFrame(rs));

		await new Promise(rs => requestAnimationFrame(rs));

		// This is a trick.
		window.getComputedStyle(target).width;

		// Now fit the terminal size.
		fit.fit();
	});

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onDestroy)(() => {
		component.off("msg:custom", cb);
		rpc.close();
	});

	function div_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			target = $$value;
			$$invalidate(0, target);
		});
	}

	$$self.$$set = $$props => {
		if ('component' in $$props) $$invalidate(1, component = $$props.component);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*target*/ 1) {
			$: if (!!target) terminal.open(target);
		}
	};

	return [target, component, div_binding];
}

class Terminal_1 extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { component: 1 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Terminal_1);

/***/ }),

/***/ "./lib/widgets/encode/Widget.svelte":
/*!******************************************!*\
  !*** ./lib/widgets/encode/Widget.svelte ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _Header_svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Header.svelte */ "./lib/widgets/encode/Header.svelte");
/* harmony import */ var _Terminal_svelte__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./Terminal.svelte */ "./lib/widgets/encode/Terminal.svelte");
/* lib/widgets/encode/Widget.svelte generated by Svelte v3.44.3 */





function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1vyoag3", ".encode.svelte-1vyoag3.svelte-1vyoag3{border:var(--jp-border-width) solid var(--jp-cell-editor-border-color);border-radius:0px;background:var(--jp-cell-editor-background);display:flex;flex-direction:column}.encode.svelte-1vyoag3>.svelte-1vyoag3{width:100%}");
}

function create_fragment(ctx) {
	let div2;
	let div0;
	let header;
	let t;
	let div1;
	let terminal;
	let current;

	header = new _Header_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]({
			props: { component: /*component*/ ctx[0] }
		});

	terminal = new _Terminal_svelte__WEBPACK_IMPORTED_MODULE_2__["default"]({
			props: { component: /*component*/ ctx[0] }
		});

	return {
		c() {
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(header.$$.fragment);
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(terminal.$$.fragment);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "svelte-1vyoag3");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "svelte-1vyoag3");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "encode svelte-1vyoag3");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, div0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(header, div0, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, t);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, div1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(terminal, div1, null);
			current = true;
		},
		p(ctx, [dirty]) {
			const header_changes = {};
			if (dirty & /*component*/ 1) header_changes.component = /*component*/ ctx[0];
			header.$set(header_changes);
			const terminal_changes = {};
			if (dirty & /*component*/ 1) terminal_changes.component = /*component*/ ctx[0];
			terminal.$set(terminal_changes);
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(header.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(terminal.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(header.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(terminal.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(header);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(terminal);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { component } = $$props;

	$$self.$$set = $$props => {
		if ('component' in $$props) $$invalidate(0, component = $$props.component);
	};

	return [component];
}

class Widget extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { component: 0 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Widget);

/***/ }),

/***/ "./lib/widgets/preview/Footer.svelte":
/*!*******************************************!*\
  !*** ./lib/widgets/preview/Footer.svelte ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _LineSlider_svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./LineSlider.svelte */ "./lib/widgets/preview/LineSlider.svelte");
/* harmony import */ var _JupyterSelect_svelte__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./JupyterSelect.svelte */ "./lib/widgets/preview/JupyterSelect.svelte");
/* lib/widgets/preview/Footer.svelte generated by Svelte v3.44.3 */





function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1uhq7gv", ".bottom.svelte-1uhq7gv.svelte-1uhq7gv{display:flex}.current-frame.svelte-1uhq7gv.svelte-1uhq7gv{line-height:100%;padding-top:4px;padding-right:5px}.current-frame.svelte-1uhq7gv>input.svelte-1uhq7gv{border:0;width:50px;text-align:right;background:transparent;color:var(--jp-widgets-color)}.line-slider.svelte-1uhq7gv.svelte-1uhq7gv{flex-grow:1;flex-shrink:1}");
}

// (5:8) {:else}
function create_else_block(ctx) {
	let input;
	let mounted;
	let dispose;

	return {
		c() {
			input = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("input");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(input, "type", "number");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(input, "class", "svelte-1uhq7gv");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, input, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_input_value)(input, /*proposedValue*/ ctx[3]);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(input, "input", /*input_input_handler_1*/ ctx[5]);
				mounted = true;
			}
		},
		p(ctx, dirty) {
			if (dirty & /*proposedValue*/ 8 && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.to_number)(input.value) !== /*proposedValue*/ ctx[3]) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_input_value)(input, /*proposedValue*/ ctx[3]);
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(input);
			mounted = false;
			dispose();
		}
	};
}

// (3:8) {#if proposedValue === null}
function create_if_block(ctx) {
	let input;
	let mounted;
	let dispose;

	return {
		c() {
			input = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("input");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(input, "type", "number");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(input, "class", "svelte-1uhq7gv");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, input, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_input_value)(input, /*frame*/ ctx[0]);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(input, "input", /*input_input_handler*/ ctx[4]);
				mounted = true;
			}
		},
		p(ctx, dirty) {
			if (dirty & /*frame*/ 1 && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.to_number)(input.value) !== /*frame*/ ctx[0]) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_input_value)(input, /*frame*/ ctx[0]);
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(input);
			mounted = false;
			dispose();
		}
	};
}

// (15:8) <JupyterSelect bind:value={ zoom }>
function create_default_slot(ctx) {
	let option0;
	let option0_value_value;
	let t1;
	let option1;
	let option1_value_value;
	let t3;
	let option2;
	let option2_value_value;
	let t5;
	let option3;
	let option3_value_value;
	let t7;
	let option4;
	let option4_value_value;
	let t9;
	let option5;
	let option5_value_value;
	let t11;
	let option6;
	let option6_value_value;

	return {
		c() {
			option0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option0.textContent = "25%";
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			option1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option1.textContent = "50%";
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			option2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option2.textContent = "75%";
			t5 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			option3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option3.textContent = "100%";
			t7 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			option4 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option4.textContent = "150%";
			t9 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			option5 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option5.textContent = "200%";
			t11 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			option6 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("option");
			option6.textContent = "300%";
			option0.__value = option0_value_value = .25;
			option0.value = option0.__value;
			option1.__value = option1_value_value = .50;
			option1.value = option1.__value;
			option2.__value = option2_value_value = .70;
			option2.value = option2.__value;
			option3.__value = option3_value_value = 1;
			option3.value = option3.__value;
			option4.__value = option4_value_value = 1.5;
			option4.value = option4.__value;
			option5.__value = option5_value_value = 2.0;
			option5.value = option5.__value;
			option6.__value = option6_value_value = 3.0;
			option6.value = option6.__value;
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option0, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t3, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t5, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option3, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t7, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option4, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t9, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option5, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t11, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, option6, anchor);
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option0);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t1);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option1);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t3);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option2);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t5);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option3);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t7);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option4);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t9);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option5);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t11);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(option6);
		}
	};
}

function create_fragment(ctx) {
	let div3;
	let div0;
	let t0;
	let t1;
	let t2;
	let div1;
	let lineslider;
	let updating_value;
	let updating_proposedValue;
	let t3;
	let div2;
	let jupyterselect;
	let updating_value_1;
	let current;

	function select_block_type(ctx, dirty) {
		if (/*proposedValue*/ ctx[3] === null) return create_if_block;
		return create_else_block;
	}

	let current_block_type = select_block_type(ctx, -1);
	let if_block = current_block_type(ctx);

	function lineslider_value_binding(value) {
		/*lineslider_value_binding*/ ctx[6](value);
	}

	function lineslider_proposedValue_binding(value) {
		/*lineslider_proposedValue_binding*/ ctx[7](value);
	}

	let lineslider_props = { min: 0, max: /*length*/ ctx[2] };

	if (/*frame*/ ctx[0] !== void 0) {
		lineslider_props.value = /*frame*/ ctx[0];
	}

	if (/*proposedValue*/ ctx[3] !== void 0) {
		lineslider_props.proposedValue = /*proposedValue*/ ctx[3];
	}

	lineslider = new _LineSlider_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]({ props: lineslider_props });
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(lineslider, 'value', lineslider_value_binding));
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(lineslider, 'proposedValue', lineslider_proposedValue_binding));

	function jupyterselect_value_binding(value) {
		/*jupyterselect_value_binding*/ ctx[8](value);
	}

	let jupyterselect_props = {
		$$slots: { default: [create_default_slot] },
		$$scope: { ctx }
	};

	if (/*zoom*/ ctx[1] !== void 0) {
		jupyterselect_props.value = /*zoom*/ ctx[1];
	}

	jupyterselect = new _JupyterSelect_svelte__WEBPACK_IMPORTED_MODULE_2__["default"]({ props: jupyterselect_props });
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(jupyterselect, 'value', jupyterselect_value_binding));

	return {
		c() {
			div3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			if_block.c();
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("\n        /\n        ");
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(/*length*/ ctx[2]);
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(lineslider.$$.fragment);
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(jupyterselect.$$.fragment);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "current-frame svelte-1uhq7gv");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "line-slider svelte-1uhq7gv");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "zoom");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div3, "class", "bottom svelte-1uhq7gv");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div3, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div0);
			if_block.m(div0, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div0, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div0, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(lineslider, div1, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t3);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(jupyterselect, div2, null);
			current = true;
		},
		p(ctx, [dirty]) {
			if (current_block_type === (current_block_type = select_block_type(ctx, dirty)) && if_block) {
				if_block.p(ctx, dirty);
			} else {
				if_block.d(1);
				if_block = current_block_type(ctx);

				if (if_block) {
					if_block.c();
					if_block.m(div0, t0);
				}
			}

			if (!current || dirty & /*length*/ 4) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t1, /*length*/ ctx[2]);
			const lineslider_changes = {};
			if (dirty & /*length*/ 4) lineslider_changes.max = /*length*/ ctx[2];

			if (!updating_value && dirty & /*frame*/ 1) {
				updating_value = true;
				lineslider_changes.value = /*frame*/ ctx[0];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_value = false);
			}

			if (!updating_proposedValue && dirty & /*proposedValue*/ 8) {
				updating_proposedValue = true;
				lineslider_changes.proposedValue = /*proposedValue*/ ctx[3];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_proposedValue = false);
			}

			lineslider.$set(lineslider_changes);
			const jupyterselect_changes = {};

			if (dirty & /*$$scope*/ 512) {
				jupyterselect_changes.$$scope = { dirty, ctx };
			}

			if (!updating_value_1 && dirty & /*zoom*/ 2) {
				updating_value_1 = true;
				jupyterselect_changes.value = /*zoom*/ ctx[1];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_value_1 = false);
			}

			jupyterselect.$set(jupyterselect_changes);
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(lineslider.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(jupyterselect.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(lineslider.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(jupyterselect.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div3);
			if_block.d();
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(lineslider);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(jupyterselect);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { frame } = $$props;
	let { length } = $$props;
	let { zoom } = $$props;
	let proposedValue;

	function input_input_handler() {
		frame = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.to_number)(this.value);
		$$invalidate(0, frame);
	}

	function input_input_handler_1() {
		proposedValue = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.to_number)(this.value);
		$$invalidate(3, proposedValue);
	}

	function lineslider_value_binding(value) {
		frame = value;
		$$invalidate(0, frame);
	}

	function lineslider_proposedValue_binding(value) {
		proposedValue = value;
		$$invalidate(3, proposedValue);
	}

	function jupyterselect_value_binding(value) {
		zoom = value;
		$$invalidate(1, zoom);
	}

	$$self.$$set = $$props => {
		if ('frame' in $$props) $$invalidate(0, frame = $$props.frame);
		if ('length' in $$props) $$invalidate(2, length = $$props.length);
		if ('zoom' in $$props) $$invalidate(1, zoom = $$props.zoom);
	};

	return [
		frame,
		zoom,
		length,
		proposedValue,
		input_input_handler,
		input_input_handler_1,
		lineslider_value_binding,
		lineslider_proposedValue_binding,
		jupyterselect_value_binding
	];
}

class Footer extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { frame: 0, length: 2, zoom: 1 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Footer);

/***/ }),

/***/ "./lib/widgets/preview/Header.svelte":
/*!*******************************************!*\
  !*** ./lib/widgets/preview/Header.svelte ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* lib/widgets/preview/Header.svelte generated by Svelte v3.44.3 */





function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1b04bb5", ".top.svelte-1b04bb5.svelte-1b04bb5{display:flex;line-height:27px;height:27px}.top.svelte-1b04bb5>.svelte-1b04bb5:not(.spacer){padding:0px 10px}.top.svelte-1b04bb5>.svelte-1b04bb5:not(:last-child){border-right:var(--jp-border-width) solid var(--jp-cell-editor-border-color)}.spacer.svelte-1b04bb5.svelte-1b04bb5{flex-grow:1;flex-shrink:1}.toolbar.svelte-1b04bb5.svelte-1b04bb5{border:0;background:transparent;margin:0;padding:0;line-height:35px}.toolbar.svelte-1b04bb5.svelte-1b04bb5:not(:last-child){padding-right:5px}");
}

// (26:4) {:else}
function create_else_block(ctx) {
	let div0;
	let t1;
	let promise;
	let t2;
	let div1;
	let button0;
	let t3;
	let div2;
	let t4;
	let div3;
	let promise_1;
	let t5;
	let div4;
	let t6;
	let div5;
	let button1;
	let t7;
	let promise_2;
	let t8;
	let div6;
	let mounted;
	let dispose;

	let info = {
		ctx,
		current: null,
		token: null,
		hasCatch: true,
		pending: create_pending_block_4,
		then: create_then_block_4,
		catch: create_catch_block_4,
		value: 16
	};

	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise = /*frameDataPromiseLeft*/ ctx[5], info);

	let info_1 = {
		ctx,
		current: null,
		token: null,
		hasCatch: false,
		pending: create_pending_block_3,
		then: create_then_block_3,
		catch: create_catch_block_3,
		value: 17
	};

	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise_1 = /*lengthPromise*/ ctx[6], info_1);

	let info_2 = {
		ctx,
		current: null,
		token: null,
		hasCatch: true,
		pending: create_pending_block_2,
		then: create_then_block_2,
		catch: create_catch_block_2,
		value: 16
	};

	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise_2 = /*frameDataPromiseRight*/ ctx[4], info_2);

	return {
		c() {
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0.textContent = "A";
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			info.block.c();
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			button0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t4 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			info_1.block.c();
			t5 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div4 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t6 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div5 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			button1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			t7 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			info_2.block.c();
			t8 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div6 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div6.textContent = "B";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button0, "class", "toolbar svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "spacer svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div3, "class", "svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div4, "class", "spacer svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button1, "class", "toolbar svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div5, "class", "svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div6, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div0, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t1, anchor);
			info.block.m(target, info.anchor = anchor);
			info.mount = () => t2.parentNode;
			info.anchor = t2;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div1, button0);
			/*button0_binding*/ ctx[13](button0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t3, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t4, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div3, anchor);
			info_1.block.m(div3, info_1.anchor = null);
			info_1.mount = () => div3;
			info_1.anchor = null;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t5, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div4, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t6, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div5, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div5, button1);
			/*button1_binding*/ ctx[15](button1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t7, anchor);
			info_2.block.m(target, info_2.anchor = anchor);
			info_2.mount = () => t8.parentNode;
			info_2.anchor = t8;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t8, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div6, anchor);

			if (!mounted) {
				dispose = [
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button0, "click", /*click_handler_1*/ ctx[12]('clip')),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button1, "click", /*click_handler_2*/ ctx[14]('diff'))
				];

				mounted = true;
			}
		},
		p(new_ctx, dirty) {
			ctx = new_ctx;
			info.ctx = ctx;

			if (dirty & /*frameDataPromiseLeft*/ 32 && promise !== (promise = /*frameDataPromiseLeft*/ ctx[5]) && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise, info)) {
				
			} else {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_await_block_branch)(info, ctx, dirty);
			}

			info_1.ctx = ctx;

			if (dirty & /*lengthPromise*/ 64 && promise_1 !== (promise_1 = /*lengthPromise*/ ctx[6]) && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise_1, info_1)) {
				
			} else {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_await_block_branch)(info_1, ctx, dirty);
			}

			info_2.ctx = ctx;

			if (dirty & /*frameDataPromiseRight*/ 16 && promise_2 !== (promise_2 = /*frameDataPromiseRight*/ ctx[4]) && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise_2, info_2)) {
				
			} else {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_await_block_branch)(info_2, ctx, dirty);
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div0);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t1);
			info.block.d(detaching);
			info.token = null;
			info = null;
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t2);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div1);
			/*button0_binding*/ ctx[13](null);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t3);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div2);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t4);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div3);
			info_1.block.d();
			info_1.token = null;
			info_1 = null;
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t5);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div4);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t6);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div5);
			/*button1_binding*/ ctx[15](null);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t7);
			info_2.block.d(detaching);
			info_2.token = null;
			info_2 = null;
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t8);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div6);
			mounted = false;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.run_all)(dispose);
		}
	};
}

// (4:30) 
function create_if_block_1(ctx) {
	let div0;
	let promise;
	let t0;
	let promise_1;
	let t1;
	let div1;
	let t2;
	let div2;
	let button;
	let mounted;
	let dispose;

	let info = {
		ctx,
		current: null,
		token: null,
		hasCatch: false,
		pending: create_pending_block_1,
		then: create_then_block_1,
		catch: create_catch_block_1,
		value: 17
	};

	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise = /*lengthPromise*/ ctx[6], info);

	let info_1 = {
		ctx,
		current: null,
		token: null,
		hasCatch: true,
		pending: create_pending_block,
		then: create_then_block,
		catch: create_catch_block,
		value: 16
	};

	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise_1 = /*frameDataPromiseLeft*/ ctx[5], info_1);

	return {
		c() {
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			info.block.c();
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			info_1.block.c();
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			button = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("button");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "spacer svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(button, "class", "toolbar svelte-1b04bb5");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div0, anchor);
			info.block.m(div0, info.anchor = null);
			info.mount = () => div0;
			info.anchor = null;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t0, anchor);
			info_1.block.m(target, info_1.anchor = anchor);
			info_1.mount = () => t1.parentNode;
			info_1.anchor = t1;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, button);
			/*button_binding*/ ctx[11](button);

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(button, "click", /*click_handler*/ ctx[10]('clip'));
				mounted = true;
			}
		},
		p(new_ctx, dirty) {
			ctx = new_ctx;
			info.ctx = ctx;

			if (dirty & /*lengthPromise*/ 64 && promise !== (promise = /*lengthPromise*/ ctx[6]) && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise, info)) {
				
			} else {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_await_block_branch)(info, ctx, dirty);
			}

			info_1.ctx = ctx;

			if (dirty & /*frameDataPromiseLeft*/ 32 && promise_1 !== (promise_1 = /*frameDataPromiseLeft*/ ctx[5]) && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise_1, info_1)) {
				
			} else {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_await_block_branch)(info_1, ctx, dirty);
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div0);
			info.block.d();
			info.token = null;
			info = null;
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t0);
			info_1.block.d(detaching);
			info_1.token = null;
			info_1 = null;
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t1);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div1);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t2);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div2);
			/*button_binding*/ ctx[11](null);
			mounted = false;
			dispose();
		}
	};
}

// (2:4) {#if clip_id == null}
function create_if_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "No image";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (36:8) {:catch}
function create_catch_block_4(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Error";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (34:8) {:then frameData}
function create_then_block_4(ctx) {
	let div;
	let t0_value = /*frameData*/ ctx[16].size[0] + "";
	let t0;
	let t1;
	let t2_value = /*frameData*/ ctx[16].size[1] + "";
	let t2;
	let t3;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t0_value);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("px × ");
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t2_value);
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("px");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t3);
		},
		p(ctx, dirty) {
			if (dirty & /*frameDataPromiseLeft*/ 32 && t0_value !== (t0_value = /*frameData*/ ctx[16].size[0] + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t0, t0_value);
			if (dirty & /*frameDataPromiseLeft*/ 32 && t2_value !== (t2_value = /*frameData*/ ctx[16].size[1] + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t2, t2_value);
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (32:37)              <div>Updating ...</div>         {:then frameData}
function create_pending_block_4(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Updating ...";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (1:0) <div class="top">     {#if clip_id == null}
function create_catch_block_3(ctx) {
	return { c: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop, m: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop, p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop, d: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop };
}

// (49:12) {:then length}
function create_then_block_3(ctx) {
	let t0_value = /*length*/ ctx[17].length + "";
	let t0;
	let t1;

	return {
		c() {
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t0_value);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(" frames");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t0, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t1, anchor);
		},
		p(ctx, dirty) {
			if (dirty & /*lengthPromise*/ 64 && t0_value !== (t0_value = /*length*/ ctx[17].length + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t0, t0_value);
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t0);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t1);
		}
	};
}

// (47:34)                  ... frames             {:then length}
function create_pending_block_3(ctx) {
	let t;

	return {
		c() {
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("... frames");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t);
		}
	};
}

// (63:8) {:catch}
function create_catch_block_2(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Error";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (61:8) {:then frameData}
function create_then_block_2(ctx) {
	let div;
	let t0_value = /*frameData*/ ctx[16].size[0] + "";
	let t0;
	let t1;
	let t2_value = /*frameData*/ ctx[16].size[1] + "";
	let t2;
	let t3;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t0_value);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("px × ");
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t2_value);
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("px");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t3);
		},
		p(ctx, dirty) {
			if (dirty & /*frameDataPromiseRight*/ 16 && t0_value !== (t0_value = /*frameData*/ ctx[16].size[0] + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t0, t0_value);
			if (dirty & /*frameDataPromiseRight*/ 16 && t2_value !== (t2_value = /*frameData*/ ctx[16].size[1] + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t2, t2_value);
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (59:38)              <div>Updating ...</div>         {:then frameData}
function create_pending_block_2(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Updating ...";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (1:0) <div class="top">     {#if clip_id == null}
function create_catch_block_1(ctx) {
	return { c: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop, m: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop, p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop, d: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop };
}

// (8:12) {:then length}
function create_then_block_1(ctx) {
	let t0_value = /*length*/ ctx[17].length + "";
	let t0;
	let t1;

	return {
		c() {
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t0_value);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(" frames");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t0, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t1, anchor);
		},
		p(ctx, dirty) {
			if (dirty & /*lengthPromise*/ 64 && t0_value !== (t0_value = /*length*/ ctx[17].length + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t0, t0_value);
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t0);
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t1);
		}
	};
}

// (6:34)                  ... frames             {:then length}
function create_pending_block_1(ctx) {
	let t;

	return {
		c() {
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("... frames");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, t, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(t);
		}
	};
}

// (16:8) {:catch}
function create_catch_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Error";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (14:8) {:then frameData}
function create_then_block(ctx) {
	let div;
	let t0_value = /*frameData*/ ctx[16].size[0] + "";
	let t0;
	let t1;
	let t2_value = /*frameData*/ ctx[16].size[1] + "";
	let t2;
	let t3;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t0_value);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("px × ");
			t2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)(t2_value);
			t3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.text)("px");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t3);
		},
		p(ctx, dirty) {
			if (dirty & /*frameDataPromiseLeft*/ 32 && t0_value !== (t0_value = /*frameData*/ ctx[16].size[0] + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t0, t0_value);
			if (dirty & /*frameDataPromiseLeft*/ 32 && t2_value !== (t2_value = /*frameData*/ ctx[16].size[1] + "")) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_data)(t2, t2_value);
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (12:37)              <div>Updating ...</div>         {:then frameData}
function create_pending_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Updating ...";
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

function create_fragment(ctx) {
	let div;

	function select_block_type(ctx, dirty) {
		if (/*clip_id*/ ctx[0] == null) return create_if_block;
		if (/*diff_id*/ ctx[1] == null) return create_if_block_1;
		return create_else_block;
	}

	let current_block_type = select_block_type(ctx, -1);
	let if_block = current_block_type(ctx);

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			if_block.c();
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "top svelte-1b04bb5");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			if_block.m(div, null);
		},
		p(ctx, [dirty]) {
			if (current_block_type === (current_block_type = select_block_type(ctx, dirty)) && if_block) {
				if_block.p(ctx, dirty);
			} else {
				if_block.d(1);
				if_block = current_block_type(ctx);

				if (if_block) {
					if_block.c();
					if_block.m(div, null);
				}
			}
		},
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
			if_block.d();
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let lengthPromise;
	let frameDataPromiseLeft;
	let frameDataPromiseRight;
	let { rpc } = $$props;
	let { frame } = $$props;
	let { clip_id } = $$props;
	let { diff_id } = $$props;
	let diffDLIcon, clipDLIcon;

	async function download(type) {
		const rawFrame = await rpc.frame({ frame, image: type });
		const blob = URL.createObjectURL(new Blob([rawFrame.buffers[0]], { type: 'image/png' }));
		const a = document.createElement("a");
		document.body.append(a);
		a.href = blob;
		a.download = `Image-${type}-${frame}.png`;
		a.click();
		await (0,svelte__WEBPACK_IMPORTED_MODULE_2__.tick)();
		URL.revokeObjectURL(blob);
		a.remove();
	}

	const click_handler = ty => () => download(ty);

	function button_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			clipDLIcon = $$value;
			$$invalidate(3, clipDLIcon);
		});
	}

	const click_handler_1 = ty => () => download(ty);

	function button0_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			clipDLIcon = $$value;
			$$invalidate(3, clipDLIcon);
		});
	}

	const click_handler_2 = ty => () => download(ty);

	function button1_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			diffDLIcon = $$value;
			$$invalidate(2, diffDLIcon);
		});
	}

	$$self.$$set = $$props => {
		if ('rpc' in $$props) $$invalidate(8, rpc = $$props.rpc);
		if ('frame' in $$props) $$invalidate(9, frame = $$props.frame);
		if ('clip_id' in $$props) $$invalidate(0, clip_id = $$props.clip_id);
		if ('diff_id' in $$props) $$invalidate(1, diff_id = $$props.diff_id);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*diff_id, clip_id, rpc*/ 259) {
			$: $$invalidate(6, lengthPromise = [diff_id, clip_id, rpc.length()][2]);
		}

		if ($$self.$$.dirty & /*diff_id, clip_id, rpc, frame*/ 771) {
			$: $$invalidate(5, frameDataPromiseLeft = [diff_id, clip_id, rpc.frame({ frame })][2]);
		}

		if ($$self.$$.dirty & /*diff_id, clip_id, rpc, frame*/ 771) {
			$: $$invalidate(4, frameDataPromiseRight = [diff_id, clip_id, rpc.frame({ frame, image: "diff" })][2]);
		}

		if ($$self.$$.dirty & /*diffDLIcon, clipDLIcon*/ 12) {
			$: [diffDLIcon, clipDLIcon].forEach(e => {
				if (!!e) _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.downloadIcon.element({
					container: e,
					width: '16px',
					height: '16px',
					marginLeft: '2px'
				});
			});
		}
	};

	return [
		clip_id,
		diff_id,
		diffDLIcon,
		clipDLIcon,
		frameDataPromiseRight,
		frameDataPromiseLeft,
		lengthPromise,
		download,
		rpc,
		frame,
		click_handler,
		button_binding,
		click_handler_1,
		button0_binding,
		click_handler_2,
		button1_binding
	];
}

class Header extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { rpc: 8, frame: 9, clip_id: 0, diff_id: 1 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Header);

/***/ }),

/***/ "./lib/widgets/preview/Image.svelte":
/*!******************************************!*\
  !*** ./lib/widgets/preview/Image.svelte ***!
  \******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* lib/widgets/preview/Image.svelte generated by Svelte v3.44.3 */




function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-30pkt", "img.zoomed.svelte-30pkt{image-rendering:pixelated}");
}

function create_fragment(ctx) {
	let img;
	let img_src_value;
	let img_alt_value;
	let img_width_value;
	let img_height_value;
	let img_class_value;

	return {
		c() {
			img = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("img");
			if (!(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.src_url_equal)(img.src, img_src_value = /*currentImageURL*/ ctx[1])) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "src", img_src_value);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "alt", img_alt_value = "Frame: " + /*frame*/ ctx[0]);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "width", img_width_value = "" + (/*size*/ ctx[3][0] + "px"));
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "height", img_height_value = "" + (/*size*/ ctx[3][1] + "px"));
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "class", img_class_value = "" + ((0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.null_to_empty)(/*extraZoomClass*/ ctx[2]) + " svelte-30pkt"));
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, img, anchor);
		},
		p(ctx, [dirty]) {
			if (dirty & /*currentImageURL*/ 2 && !(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.src_url_equal)(img.src, img_src_value = /*currentImageURL*/ ctx[1])) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "src", img_src_value);
			}

			if (dirty & /*frame*/ 1 && img_alt_value !== (img_alt_value = "Frame: " + /*frame*/ ctx[0])) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "alt", img_alt_value);
			}

			if (dirty & /*size*/ 8 && img_width_value !== (img_width_value = "" + (/*size*/ ctx[3][0] + "px"))) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "width", img_width_value);
			}

			if (dirty & /*size*/ 8 && img_height_value !== (img_height_value = "" + (/*size*/ ctx[3][1] + "px"))) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "height", img_height_value);
			}

			if (dirty & /*extraZoomClass*/ 4 && img_class_value !== (img_class_value = "" + ((0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.null_to_empty)(/*extraZoomClass*/ ctx[2]) + " svelte-30pkt"))) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(img, "class", img_class_value);
			}
		},
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(img);
		}
	};
}

function scaleSize(sz, factor) {
	return [
		Math.max(1, Math.floor(sz[0] * factor)),
		Math.max(1, Math.floor(sz[1] * factor))
	];
}

function instance($$self, $$props, $$invalidate) {
	let zoomFactor;
	let size;
	let extraZoomClass;
	let { rpc } = $$props;
	let { frame } = $$props;
	let { type = "clip" } = $$props;
	let { zoom = 1 } = $$props;
	let currentSize = [1, 1];
	let currentImageURL = null;
	let nextRequestFrame = null;
	let currentPromise = null;
	let pixelRatio = window.devicePixelRatio;

	let pixelRatioInterval = setInterval(1000, () => {
		$$invalidate(8, pixelRatio = window.devicePixelRatio);
	});

	function updateByFrameNo() {
		nextRequestFrame = frame;
		requestNext();
	}

	function requestNext() {
		if (currentPromise !== null) return;
		const currentFrame = nextRequestFrame;
		currentPromise = rpc.frame({ frame, image: type });

		currentPromise.then(() => {
			currentPromise = null;
			if (nextRequestFrame === currentFrame) return;
			requestNext();
		});

		currentPromise.then(({ size, buffers }) => {
			destroyExistingBlob();
			$$invalidate(1, currentImageURL = URL.createObjectURL(new Blob([buffers[0]], { type: "application/json" })));
			$$invalidate(7, currentSize = size);
		});

		currentPromise.catch(console.error);
	}

	function destroyExistingBlob() {
		if (currentImageURL !== null) {
			URL.revokeObjectURL(currentImageURL);
			$$invalidate(1, currentImageURL = null);
		}
	}

	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onDestroy)(() => {
		destroyExistingBlob();
		clearInterval(pixelRatioInterval);
	});

	$$self.$$set = $$props => {
		if ('rpc' in $$props) $$invalidate(4, rpc = $$props.rpc);
		if ('frame' in $$props) $$invalidate(0, frame = $$props.frame);
		if ('type' in $$props) $$invalidate(5, type = $$props.type);
		if ('zoom' in $$props) $$invalidate(6, zoom = $$props.zoom);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*frame*/ 1) {
			$: updateByFrameNo(frame);
		}

		if ($$self.$$.dirty & /*zoom, pixelRatio*/ 320) {
			$: $$invalidate(9, zoomFactor = zoom / pixelRatio);
		}

		if ($$self.$$.dirty & /*currentSize, zoomFactor*/ 640) {
			$: $$invalidate(3, size = scaleSize(currentSize, zoomFactor));
		}

		if ($$self.$$.dirty & /*zoom*/ 64) {
			$: $$invalidate(2, extraZoomClass = zoom != 1 ? "zoomed" : "");
		}
	};

	return [
		frame,
		currentImageURL,
		extraZoomClass,
		size,
		rpc,
		type,
		zoom,
		currentSize,
		pixelRatio,
		zoomFactor
	];
}

class Image extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { rpc: 4, frame: 0, type: 5, zoom: 6 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Image);

/***/ }),

/***/ "./lib/widgets/preview/JupyterSelect.svelte":
/*!**************************************************!*\
  !*** ./lib/widgets/preview/JupyterSelect.svelte ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* lib/widgets/preview/JupyterSelect.svelte generated by Svelte v3.44.3 */




function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1gk8783", ".yuuno-fake.svelte-1gk8783{display:flex}");
}

function create_fragment(ctx) {
	let div;
	let select;
	let t;
	let span;
	let current;
	let mounted;
	let dispose;
	const default_slot_template = /*#slots*/ ctx[4].default;
	const default_slot = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_slot)(default_slot_template, ctx, /*$$scope*/ ctx[3], null);

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			select = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("select");
			if (default_slot) default_slot.c();
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			span = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("span");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(select, "title", /*title*/ ctx[1]);
			if (/*value*/ ctx[0] === void 0) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_render_callback)(() => /*select_change_handler*/ ctx[5].call(select));
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "jp-HTMLSelect jp-DefaultStyle jp-Notebook-toolbarCellTypeDropdown yuuno-fake svelte-1gk8783");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, select);

			if (default_slot) {
				default_slot.m(select, null);
			}

			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.select_option)(select, /*value*/ ctx[0]);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, t);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div, span);
			/*span_binding*/ ctx[6](span);
			current = true;

			if (!mounted) {
				dispose = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(select, "change", /*select_change_handler*/ ctx[5]);
				mounted = true;
			}
		},
		p(ctx, [dirty]) {
			if (default_slot) {
				if (default_slot.p && (!current || dirty & /*$$scope*/ 8)) {
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_slot_base)(
						default_slot,
						default_slot_template,
						ctx,
						/*$$scope*/ ctx[3],
						!current
						? (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.get_all_dirty_from_scope)(/*$$scope*/ ctx[3])
						: (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.get_slot_changes)(default_slot_template, /*$$scope*/ ctx[3], dirty, null),
						null
					);
				}
			}

			if (!current || dirty & /*title*/ 2) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(select, "title", /*title*/ ctx[1]);
			}

			if (dirty & /*value*/ 1) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.select_option)(select, /*value*/ ctx[0]);
			}
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(default_slot, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(default_slot, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
			if (default_slot) default_slot.d(detaching);
			/*span_binding*/ ctx[6](null);
			mounted = false;
			dispose();
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let { $$slots: slots = {}, $$scope } = $$props;
	let { title = "" } = $$props;
	let { value } = $$props;
	let iconTarget;

	function select_change_handler() {
		value = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.select_value)(this);
		$$invalidate(0, value);
	}

	function span_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			iconTarget = $$value;
			$$invalidate(2, iconTarget);
		});
	}

	$$self.$$set = $$props => {
		if ('title' in $$props) $$invalidate(1, title = $$props.title);
		if ('value' in $$props) $$invalidate(0, value = $$props.value);
		if ('$$scope' in $$props) $$invalidate(3, $$scope = $$props.$$scope);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*iconTarget*/ 4) {
			$: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretDownEmptyIcon.element({
				container: iconTarget,
				width: '16px',
				height: '16px',
				marginLeft: '2px'
			});
		}
	};

	return [value, title, iconTarget, $$scope, slots, select_change_handler, span_binding];
}

class JupyterSelect extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { title: 1, value: 0 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (JupyterSelect);

/***/ }),

/***/ "./lib/widgets/preview/LineSlider.svelte":
/*!***********************************************!*\
  !*** ./lib/widgets/preview/LineSlider.svelte ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* lib/widgets/preview/LineSlider.svelte generated by Svelte v3.44.3 */


function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-kk8zs1", ".line-slider.svelte-kk8zs1.svelte-kk8zs1{position:relative;width:100%;height:100%;display:block;border-left:var(--jp-border-width) solid var(--jp-cell-editor-border-color);border-right:var(--jp-border-width) solid var(--jp-cell-editor-border-color)}.line-slider.svelte-kk8zs1>.svelte-kk8zs1{position:absolute;height:20%;bottom:0}.past.svelte-kk8zs1.svelte-kk8zs1{left:0;background-color:var(--jp-brand-color1)}.future.svelte-kk8zs1.svelte-kk8zs1{right:0;background-color:var(--jp-cell-editor-border-color)}.select.svelte-kk8zs1.svelte-kk8zs1,.proposed.svelte-kk8zs1.svelte-kk8zs1{height:100%;top:0;width:var(--jp-border-width);background-color:var(--jp-brand-color1)}");
}

// (5:4) {:else}
function create_else_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "proposed svelte-kk8zs1");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*proposedPerc*/ ctx[1] * 100 + "%");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p(ctx, dirty) {
			if (dirty & /*proposedPerc*/ 2) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*proposedPerc*/ ctx[1] * 100 + "%");
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

// (3:4) {#if proposedValue === null}
function create_if_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "select svelte-kk8zs1");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*percPast*/ ctx[2] * 100 + "%");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p(ctx, dirty) {
			if (dirty & /*percPast*/ 4) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div, "left", /*percPast*/ ctx[2] * 100 + "%");
			}
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

function create_fragment(ctx) {
	let div2;
	let div0;
	let t0;
	let t1;
	let div1;
	let mounted;
	let dispose;

	function select_block_type(ctx, dirty) {
		if (/*proposedValue*/ ctx[0] === null) return create_if_block;
		return create_else_block;
	}

	let current_block_type = select_block_type(ctx, -1);
	let if_block = current_block_type(ctx);

	return {
		c() {
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			if_block.c();
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "past svelte-kk8zs1");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div0, "width", /*percPast*/ ctx[2] * 100 + "%");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "future svelte-kk8zs1");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div1, "width", /*percFuture*/ ctx[4] * 100 + "%");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "line-slider svelte-kk8zs1");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div2, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, div0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, t0);
			if_block.m(div2, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div2, div1);
			/*div2_binding*/ ctx[13](div2);

			if (!mounted) {
				dispose = [
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "mouseenter", /*enter*/ ctx[5]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "mouseleave", /*leave*/ ctx[6]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "mousemove", /*move*/ ctx[7]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div2, "click", /*submit*/ ctx[8])
				];

				mounted = true;
			}
		},
		p(ctx, [dirty]) {
			if (dirty & /*percPast*/ 4) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div0, "width", /*percPast*/ ctx[2] * 100 + "%");
			}

			if (current_block_type === (current_block_type = select_block_type(ctx, dirty)) && if_block) {
				if_block.p(ctx, dirty);
			} else {
				if_block.d(1);
				if_block = current_block_type(ctx);

				if (if_block) {
					if_block.c();
					if_block.m(div2, t1);
				}
			}

			if (dirty & /*percFuture*/ 16) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.set_style)(div1, "width", /*percFuture*/ ctx[4] * 100 + "%");
			}
		},
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div2);
			if_block.d();
			/*div2_binding*/ ctx[13](null);
			mounted = false;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.run_all)(dispose);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let span;
	let percPast;
	let percFuture;
	let { value = 0 } = $$props;
	let { max = 100 } = $$props;
	let { min = 0 } = $$props;
	let { proposedValue = null } = $$props;
	let { proposedPerc = null } = $$props;
	let myself;

	function enter(event) {
		$$invalidate(0, proposedValue = min);
		move(event);
	}

	function leave() {
		$$invalidate(0, proposedValue = null);
	}

	function move(event) {
		const { pageX, pageY } = event;
		const { left, top, right } = myself.getBoundingClientRect();
		const width = right - left;
		const vX = pageX - left;
		$$invalidate(1, proposedPerc = vX / width);
		const rawProposal = proposedPerc * span + min;
		$$invalidate(0, proposedValue = Math.round(rawProposal));
	}

	function submit() {
		$$invalidate(9, value = proposedValue);
	}

	function div2_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			myself = $$value;
			$$invalidate(3, myself);
		});
	}

	$$self.$$set = $$props => {
		if ('value' in $$props) $$invalidate(9, value = $$props.value);
		if ('max' in $$props) $$invalidate(10, max = $$props.max);
		if ('min' in $$props) $$invalidate(11, min = $$props.min);
		if ('proposedValue' in $$props) $$invalidate(0, proposedValue = $$props.proposedValue);
		if ('proposedPerc' in $$props) $$invalidate(1, proposedPerc = $$props.proposedPerc);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*max, min*/ 3072) {
			$: $$invalidate(12, span = max - min);
		}

		if ($$self.$$.dirty & /*value, min, span*/ 6656) {
			$: $$invalidate(2, percPast = (value - min) / span);
		}

		if ($$self.$$.dirty & /*percPast*/ 4) {
			$: $$invalidate(4, percFuture = 1 - percPast);
		}
	};

	return [
		proposedValue,
		proposedPerc,
		percPast,
		myself,
		percFuture,
		enter,
		leave,
		move,
		submit,
		value,
		max,
		min,
		span,
		div2_binding
	];
}

class LineSlider extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();

		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(
			this,
			options,
			instance,
			create_fragment,
			svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal,
			{
				value: 9,
				max: 10,
				min: 11,
				proposedValue: 0,
				proposedPerc: 1
			},
			add_css
		);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (LineSlider);

/***/ }),

/***/ "./lib/widgets/preview/Viewport.svelte":
/*!*********************************************!*\
  !*** ./lib/widgets/preview/Viewport.svelte ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _Image_svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./Image.svelte */ "./lib/widgets/preview/Image.svelte");
/* lib/widgets/preview/Viewport.svelte generated by Svelte v3.44.3 */




function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-19n1gk", ".viewport.svelte-19n1gk.svelte-19n1gk{display:flex;flex-grow:1;flex-shrink:1;background-image:linear-gradient(45deg, #808080 25%, transparent 25%),\n            linear-gradient(-45deg, #808080 25%, transparent 25%),\n            linear-gradient(45deg, transparent 75%, #808080 75%),\n            linear-gradient(-45deg, transparent 75%, #808080 75%);background-size:20px 20px;background-position:0 0, 0 10px, 10px -10px, -10px 0px;overflow:auto}.zero-sizer.svelte-19n1gk.svelte-19n1gk{position:relative;width:0;height:0}.zero-sizer.svelte-19n1gk>.item.svelte-19n1gk{position:absolute;top:0;left:0}.item.main.svelte-19n1gk.svelte-19n1gk,.item.diff.svelte-19n1gk.svelte-19n1gk{display:none}.main.svelte-19n1gk>.item.main.svelte-19n1gk{display:block}.diff.svelte-19n1gk>.item.diff.svelte-19n1gk{display:block}");
}

// (3:8) {#if clip_id !== null}
function create_if_block_1(ctx) {
	let div;
	let image;
	let current;

	image = new _Image_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]({
			props: {
				rpc: /*rpc*/ ctx[0],
				frame: /*frame*/ ctx[1],
				zoom: /*zoom*/ ctx[2],
				type: "clip"
			}
		});

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(image.$$.fragment);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "item main svelte-19n1gk");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(image, div, null);
			current = true;
		},
		p(ctx, dirty) {
			const image_changes = {};
			if (dirty & /*rpc*/ 1) image_changes.rpc = /*rpc*/ ctx[0];
			if (dirty & /*frame*/ 2) image_changes.frame = /*frame*/ ctx[1];
			if (dirty & /*zoom*/ 4) image_changes.zoom = /*zoom*/ ctx[2];
			image.$set(image_changes);
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(image.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(image.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(image);
		}
	};
}

// (9:8) {#if diff_id !== null}
function create_if_block(ctx) {
	let div;
	let image;
	let current;

	image = new _Image_svelte__WEBPACK_IMPORTED_MODULE_1__["default"]({
			props: {
				rpc: /*rpc*/ ctx[0],
				frame: /*frame*/ ctx[1],
				zoom: /*zoom*/ ctx[2],
				type: "diff"
			}
		});

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(image.$$.fragment);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div, "class", "item diff svelte-19n1gk");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(image, div, null);
			current = true;
		},
		p(ctx, dirty) {
			const image_changes = {};
			if (dirty & /*rpc*/ 1) image_changes.rpc = /*rpc*/ ctx[0];
			if (dirty & /*frame*/ 2) image_changes.frame = /*frame*/ ctx[1];
			if (dirty & /*zoom*/ 4) image_changes.zoom = /*zoom*/ ctx[2];
			image.$set(image_changes);
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(image.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(image.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(image);
		}
	};
}

function create_fragment(ctx) {
	let div1;
	let div0;
	let t;
	let div0_class_value;
	let current;
	let mounted;
	let dispose;
	let if_block0 = /*clip_id*/ ctx[3] !== null && create_if_block_1(ctx);
	let if_block1 = /*diff_id*/ ctx[4] !== null && create_if_block(ctx);

	return {
		c() {
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			if (if_block0) if_block0.c();
			t = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			if (if_block1) if_block1.c();
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", div0_class_value = "zero-sizer " + /*mode*/ ctx[6] + " svelte-19n1gk");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "viewport svelte-19n1gk");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div1, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div1, div0);
			if (if_block0) if_block0.m(div0, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div0, t);
			if (if_block1) if_block1.m(div0, null);
			/*div1_binding*/ ctx[16](div1);
			current = true;

			if (!mounted) {
				dispose = [
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div1, "mouseenter", /*enter*/ ctx[7]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div1, "mouseleave", /*leave*/ ctx[8]),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div1, "mousedown", (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.stop_propagation)((0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.prevent_default)(/*down*/ ctx[9])), true),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div1, "mouseup", (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.stop_propagation)((0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.prevent_default)(/*up*/ ctx[10])), true),
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.listen)(div1, "mousemove", /*move*/ ctx[11])
				];

				mounted = true;
			}
		},
		p(ctx, [dirty]) {
			if (/*clip_id*/ ctx[3] !== null) {
				if (if_block0) {
					if_block0.p(ctx, dirty);

					if (dirty & /*clip_id*/ 8) {
						(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(if_block0, 1);
					}
				} else {
					if_block0 = create_if_block_1(ctx);
					if_block0.c();
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(if_block0, 1);
					if_block0.m(div0, t);
				}
			} else if (if_block0) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.group_outros)();

				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(if_block0, 1, 1, () => {
					if_block0 = null;
				});

				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.check_outros)();
			}

			if (/*diff_id*/ ctx[4] !== null) {
				if (if_block1) {
					if_block1.p(ctx, dirty);

					if (dirty & /*diff_id*/ 16) {
						(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(if_block1, 1);
					}
				} else {
					if_block1 = create_if_block(ctx);
					if_block1.c();
					(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(if_block1, 1);
					if_block1.m(div0, null);
				}
			} else if (if_block1) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.group_outros)();

				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(if_block1, 1, 1, () => {
					if_block1 = null;
				});

				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.check_outros)();
			}

			if (!current || dirty & /*mode*/ 64 && div0_class_value !== (div0_class_value = "zero-sizer " + /*mode*/ ctx[6] + " svelte-19n1gk")) {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", div0_class_value);
			}
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(if_block0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(if_block1);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(if_block0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(if_block1);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div1);
			if (if_block0) if_block0.d();
			if (if_block1) if_block1.d();
			/*div1_binding*/ ctx[16](null);
			mounted = false;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.run_all)(dispose);
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let single_clip;
	let single_clip_mode;
	let multi_clip_mode;
	let mode;
	let { rpc } = $$props;
	let { frame } = $$props;
	let { zoom = 1 } = $$props;
	let { clip_id, diff_id } = $$props;
	let myself;
	let entered = false;

	function enter() {
		$$invalidate(12, entered = true);
	}

	function leave() {
		$$invalidate(12, entered = false);
	}

	let panning = null;

	function down(event) {
		panning = [event.screenX, event.screenY, myself.scrollLeft, myself.scrollTop];
	}

	function up() {
		panning = null;
	}

	function move(event) {
		if (panning === null) return;
		const { screenX, screenY } = event;
		const [startX, startY, scrollLeft, scrollTop] = panning;
		const dX = startX - screenX;
		const dY = startY - screenY;
		$$invalidate(5, myself.scrollLeft = scrollLeft + dX, myself);
		$$invalidate(5, myself.scrollTop = scrollTop + dY, myself);
	}

	function div1_binding($$value) {
		svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks[$$value ? 'unshift' : 'push'](() => {
			myself = $$value;
			$$invalidate(5, myself);
		});
	}

	$$self.$$set = $$props => {
		if ('rpc' in $$props) $$invalidate(0, rpc = $$props.rpc);
		if ('frame' in $$props) $$invalidate(1, frame = $$props.frame);
		if ('zoom' in $$props) $$invalidate(2, zoom = $$props.zoom);
		if ('clip_id' in $$props) $$invalidate(3, clip_id = $$props.clip_id);
		if ('diff_id' in $$props) $$invalidate(4, diff_id = $$props.diff_id);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*clip_id, diff_id*/ 24) {
			$: $$invalidate(15, single_clip = clip_id === null != (diff_id === null));
		}

		if ($$self.$$.dirty & /*clip_id*/ 8) {
			$: $$invalidate(14, single_clip_mode = clip_id !== null ? "main" : "diff");
		}

		if ($$self.$$.dirty & /*entered*/ 4096) {
			$: $$invalidate(13, multi_clip_mode = entered ? "diff" : "main");
		}

		if ($$self.$$.dirty & /*single_clip, single_clip_mode, multi_clip_mode*/ 57344) {
			$: $$invalidate(6, mode = single_clip ? single_clip_mode : multi_clip_mode);
		}
	};

	return [
		rpc,
		frame,
		zoom,
		clip_id,
		diff_id,
		myself,
		mode,
		enter,
		leave,
		down,
		up,
		move,
		entered,
		multi_clip_mode,
		single_clip_mode,
		single_clip,
		div1_binding
	];
}

class Viewport extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();

		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(
			this,
			options,
			instance,
			create_fragment,
			svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal,
			{
				rpc: 0,
				frame: 1,
				zoom: 2,
				clip_id: 3,
				diff_id: 4
			},
			add_css
		);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Viewport);

/***/ }),

/***/ "./lib/widgets/preview/Widget.svelte":
/*!*******************************************!*\
  !*** ./lib/widgets/preview/Widget.svelte ***!
  \*******************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var svelte_internal__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! svelte/internal */ "./node_modules/svelte/internal/index.mjs");
/* harmony import */ var _Header_svelte__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./Header.svelte */ "./lib/widgets/preview/Header.svelte");
/* harmony import */ var _Viewport_svelte__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./Viewport.svelte */ "./lib/widgets/preview/Viewport.svelte");
/* harmony import */ var _Footer_svelte__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./Footer.svelte */ "./lib/widgets/preview/Footer.svelte");
/* harmony import */ var _utils__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../../utils */ "./lib/utils.js");
/* harmony import */ var _rpc__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./rpc */ "./lib/widgets/preview/rpc.js");
/* harmony import */ var svelte__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! svelte */ "./node_modules/svelte/index.mjs");
/* lib/widgets/preview/Widget.svelte generated by Svelte v3.44.3 */









function add_css(target) {
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append_styles)(target, "svelte-1nz724k", ".preview.svelte-1nz724k.svelte-1nz724k{border:var(--jp-border-width) solid var(--jp-cell-editor-border-color);border-radius:0px;background:var(--jp-cell-editor-background);display:flex;flex-direction:column}.preview.svelte-1nz724k>.svelte-1nz724k{width:100%}.viewport.svelte-1nz724k.svelte-1nz724k{min-height:640px;flex-grow:1;flex-shrink:1;display:flex;flex-direction:column}");
}

// (1:0)  {#await currentPreview}
function create_catch_block(ctx) {
	return {
		c: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		m: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop
	};
}

// (4:0) {:then length}
function create_then_block(ctx) {
	let div3;
	let div0;
	let header;
	let t0;
	let div1;
	let viewport;
	let t1;
	let div2;
	let footer;
	let updating_frame;
	let updating_zoom;
	let current;

	header = new _Header_svelte__WEBPACK_IMPORTED_MODULE_2__["default"]({
			props: {
				clip_id: /*$clip_id*/ ctx[1],
				diff_id: /*$diff_id*/ ctx[0],
				rpc: /*preview*/ ctx[9],
				frame: /*$frame*/ ctx[3]
			}
		});

	viewport = new _Viewport_svelte__WEBPACK_IMPORTED_MODULE_3__["default"]({
			props: {
				clip_id: /*$clip_id*/ ctx[1],
				diff_id: /*$diff_id*/ ctx[0],
				rpc: /*preview*/ ctx[9],
				frame: /*$frame*/ ctx[3],
				zoom: /*$zoom*/ ctx[4]
			}
		});

	function footer_frame_binding(value) {
		/*footer_frame_binding*/ ctx[11](value);
	}

	function footer_zoom_binding(value) {
		/*footer_zoom_binding*/ ctx[12](value);
	}

	let footer_props = { length: /*length*/ ctx[14].length };

	if (/*$frame*/ ctx[3] !== void 0) {
		footer_props.frame = /*$frame*/ ctx[3];
	}

	if (/*$zoom*/ ctx[4] !== void 0) {
		footer_props.zoom = /*$zoom*/ ctx[4];
	}

	footer = new _Footer_svelte__WEBPACK_IMPORTED_MODULE_4__["default"]({ props: footer_props });
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(footer, 'frame', footer_frame_binding));
	svelte_internal__WEBPACK_IMPORTED_MODULE_0__.binding_callbacks.push(() => (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.bind)(footer, 'zoom', footer_zoom_binding));

	return {
		c() {
			div3 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(header.$$.fragment);
			t0 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(viewport.$$.fragment);
			t1 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.space)();
			div2 = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.create_component)(footer.$$.fragment);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div0, "class", "header svelte-1nz724k");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div1, "class", "viewport svelte-1nz724k");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div2, "class", "footer svelte-1nz724k");
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.attr)(div3, "class", "preview svelte-1nz724k");
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div3, anchor);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(header, div0, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t0);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(viewport, div1, null);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, t1);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.append)(div3, div2);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.mount_component)(footer, div2, null);
			current = true;
		},
		p(ctx, dirty) {
			const header_changes = {};
			if (dirty & /*$clip_id*/ 2) header_changes.clip_id = /*$clip_id*/ ctx[1];
			if (dirty & /*$diff_id*/ 1) header_changes.diff_id = /*$diff_id*/ ctx[0];
			if (dirty & /*$frame*/ 8) header_changes.frame = /*$frame*/ ctx[3];
			header.$set(header_changes);
			const viewport_changes = {};
			if (dirty & /*$clip_id*/ 2) viewport_changes.clip_id = /*$clip_id*/ ctx[1];
			if (dirty & /*$diff_id*/ 1) viewport_changes.diff_id = /*$diff_id*/ ctx[0];
			if (dirty & /*$frame*/ 8) viewport_changes.frame = /*$frame*/ ctx[3];
			if (dirty & /*$zoom*/ 16) viewport_changes.zoom = /*$zoom*/ ctx[4];
			viewport.$set(viewport_changes);
			const footer_changes = {};
			if (dirty & /*currentPreview*/ 4) footer_changes.length = /*length*/ ctx[14].length;

			if (!updating_frame && dirty & /*$frame*/ 8) {
				updating_frame = true;
				footer_changes.frame = /*$frame*/ ctx[3];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_frame = false);
			}

			if (!updating_zoom && dirty & /*$zoom*/ 16) {
				updating_zoom = true;
				footer_changes.zoom = /*$zoom*/ ctx[4];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.add_flush_callback)(() => updating_zoom = false);
			}

			footer.$set(footer_changes);
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(header.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(viewport.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(footer.$$.fragment, local);
			current = true;
		},
		o(local) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(header.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(viewport.$$.fragment, local);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(footer.$$.fragment, local);
			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div3);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(header);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(viewport);
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.destroy_component)(footer);
		}
	};
}

// (2:23)      <div>Loading ...</div> {:then length}
function create_pending_block(ctx) {
	let div;

	return {
		c() {
			div = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.element)("div");
			div.textContent = "Loading ...";
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, div, anchor);
		},
		p: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		i: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		o: svelte_internal__WEBPACK_IMPORTED_MODULE_0__.noop,
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(div);
		}
	};
}

function create_fragment(ctx) {
	let await_block_anchor;
	let promise;
	let current;

	let info = {
		ctx,
		current: null,
		token: null,
		hasCatch: false,
		pending: create_pending_block,
		then: create_then_block,
		catch: create_catch_block,
		value: 14,
		blocks: [,,,]
	};

	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise = /*currentPreview*/ ctx[2], info);

	return {
		c() {
			await_block_anchor = (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.empty)();
			info.block.c();
		},
		m(target, anchor) {
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.insert)(target, await_block_anchor, anchor);
			info.block.m(target, info.anchor = anchor);
			info.mount = () => await_block_anchor.parentNode;
			info.anchor = await_block_anchor;
			current = true;
		},
		p(new_ctx, [dirty]) {
			ctx = new_ctx;
			info.ctx = ctx;

			if (dirty & /*currentPreview*/ 4 && promise !== (promise = /*currentPreview*/ ctx[2]) && (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.handle_promise)(promise, info)) {
				
			} else {
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.update_await_block_branch)(info, ctx, dirty);
			}
		},
		i(local) {
			if (current) return;
			(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_in)(info.block);
			current = true;
		},
		o(local) {
			for (let i = 0; i < 3; i += 1) {
				const block = info.blocks[i];
				(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.transition_out)(block);
			}

			current = false;
		},
		d(detaching) {
			if (detaching) (0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.detach)(await_block_anchor);
			info.block.d(detaching);
			info.token = null;
			info = null;
		}
	};
}

function instance($$self, $$props, $$invalidate) {
	let currentPreview;
	let $diff_id;
	let $clip_id;
	let $frame;
	let $zoom;
	let { component } = $$props;
	const frame = (0,_utils__WEBPACK_IMPORTED_MODULE_5__.model_attribute)(component, "frame");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, frame, value => $$invalidate(3, $frame = value));
	const zoom = (0,_utils__WEBPACK_IMPORTED_MODULE_5__.model_attribute)(component, "zoom");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, zoom, value => $$invalidate(4, $zoom = value));
	const clip_id = (0,_utils__WEBPACK_IMPORTED_MODULE_5__.model_attribute)(component, "clip");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, clip_id, value => $$invalidate(1, $clip_id = value));
	const diff_id = (0,_utils__WEBPACK_IMPORTED_MODULE_5__.model_attribute)(component, "diff");
	(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.component_subscribe)($$self, diff_id, value => $$invalidate(0, $diff_id = value));
	const debouncedFrame = (0,_utils__WEBPACK_IMPORTED_MODULE_5__.debounce)(100, frame);
	const preview = (0,_rpc__WEBPACK_IMPORTED_MODULE_6__.getRPCForModel)(component);
	preview.open();
	(0,svelte__WEBPACK_IMPORTED_MODULE_1__.onDestroy)(() => preview.close());

	function footer_frame_binding(value) {
		$frame = value;
		frame.set($frame);
	}

	function footer_zoom_binding(value) {
		$zoom = value;
		zoom.set($zoom);
	}

	$$self.$$set = $$props => {
		if ('component' in $$props) $$invalidate(10, component = $$props.component);
	};

	$$self.$$.update = () => {
		if ($$self.$$.dirty & /*$clip_id, $diff_id*/ 3) {
			$: $$invalidate(2, currentPreview = [$clip_id, $diff_id, preview.length()][2]);
		}

		if ($$self.$$.dirty & /*component*/ 1024) {
			$: console.log(component);
		}
	};

	return [
		$diff_id,
		$clip_id,
		currentPreview,
		$frame,
		$zoom,
		frame,
		zoom,
		clip_id,
		diff_id,
		preview,
		component,
		footer_frame_binding,
		footer_zoom_binding
	];
}

class Widget extends svelte_internal__WEBPACK_IMPORTED_MODULE_0__.SvelteComponent {
	constructor(options) {
		super();
		(0,svelte_internal__WEBPACK_IMPORTED_MODULE_0__.init)(this, options, instance, create_fragment, svelte_internal__WEBPACK_IMPORTED_MODULE_0__.safe_not_equal, { component: 10 }, add_css);
	}
}

/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (Widget);

/***/ })

}]);
//# sourceMappingURL=lib_index_js.8261d50cfcdd262765d1.js.map
import{e as t,d as e,t as o,b as i,r as s,_ as r,a,c as n,n as c,s as l,$ as d}from"./index-acc71b99.js";import{g as p}from"./c.75023507.js";import"./c.6aeb6c9e.js";import{E as h,c as m}from"./c.9b8e48ba.js";import{m as u,s as _,a as w}from"./c.0ba40d5f.js";import{c as g,g as v}from"./c.a0f0ec15.js";class b{constructor(t){this.U=t}disconnect(){this.U=void 0}reconnect(t){this.U=t}deref(){return this.U}}class f{constructor(){this.Y=void 0,this.q=void 0}get(){return this.Y}pause(){var t;null!==(t=this.Y)&&void 0!==t||(this.Y=new Promise((t=>this.q=t)))}resume(){var t;null===(t=this.q)||void 0===t||t.call(this),this.Y=this.q=void 0}}const $=t=>!o(t)&&"function"==typeof t.then;const y=t(class extends e{constructor(){super(...arguments),this._$Cft=1073741823,this._$Cwt=[],this._$CG=new b(this),this._$CK=new f}render(...t){var e;return null!==(e=t.find((t=>!$(t))))&&void 0!==e?e:i}update(t,e){const o=this._$Cwt;let s=o.length;this._$Cwt=e;const r=this._$CG,a=this._$CK;this.isConnected||this.disconnected();for(let t=0;t<e.length&&!(t>this._$Cft);t++){const i=e[t];if(!$(i))return this._$Cft=t,i;t<s&&i===o[t]||(this._$Cft=1073741823,s=0,Promise.resolve(i).then((async t=>{for(;a.get();)await a.get();const e=r.deref();if(void 0!==e){const o=e._$Cwt.indexOf(i);o>-1&&o<e._$Cft&&(e._$Cft=o,e.setValue(t))}})))}return i}disconnected(){this._$CG.disconnect(),this._$CK.pause()}reconnected(){this._$CG.reconnect(this),this._$CK.resume()}}),C=(t,e)=>{import("./c.c5270900.js");const o=document.createElement("esphome-install-server-dialog");o.configuration=t,o.target=e,document.body.append(o)},k=(t,e)=>{import("./c.430c28a5.js");const o=document.createElement("esphome-compile-dialog");o.configuration=t,o.downloadFactoryFirmware=e,document.body.append(o)},S=async t=>{import("./c.1dd76054.js");const e=document.createElement("esphome-no-port-picked-dialog");return e.doTryAgain=t,document.body.append(e),!0},P=async(t,e)=>{let o;if(import("./c.c49a3e69.js"),t.port)o=new h(t.port,console);else try{o=await m(console)}catch(o){return void("NotFoundError"===o.name?S((()=>P(t,e))):alert(`Unable to connect: ${o.message}`))}e&&e();const i=document.createElement("esphome-install-web-dialog");i.params=t,i.esploader=o,document.body.append(i)};let x=class extends l{constructor(){super(...arguments),this._state="pick_option"}render(){let t,e;return"pick_option"===this._state?(t="How do you want to install this on your ESP device?",e=d`
        <mwc-list-item
          twoline
          hasMeta
          .port=${"OTA"}
          @click=${this._handleLegacyOption}
        >
          <span>Wirelessly</span>
          <span slot="secondary">Requires the device to be online</span>
          ${u}
        </mwc-list-item>

        ${this._error?d`<div class="error">${this._error}</div>`:""}

        <mwc-list-item twoline hasMeta @click=${this._handleBrowserInstall}>
          <span>Plug into this computer</span>
          <span slot="secondary">
            For devices connected via USB to this computer
          </span>
          ${u}
        </mwc-list-item>

        <mwc-list-item twoline hasMeta @click=${this._showServerPorts}>
          <span>Plug into the computer running ESPHome Dashboard</span>
          <span slot="secondary">
            For devices connected via USB to the server
          </span>
          ${u}
        </mwc-list-item>

        <mwc-list-item
          twoline
          hasMeta
          dialogAction="close"
          @click=${this._handleManualDownload}
        >
          <span>Manual download</span>
          <span slot="secondary">
            Install it yourself using ESPHome Flasher or other tools
          </span>
          ${u}
        </mwc-list-item>

        <mwc-button
          no-attention
          slot="secondaryAction"
          dialogAction="close"
          label="Cancel"
        ></mwc-button>
      `):"pick_server_port"===this._state?(t="Pick Server Port",e=void 0===this._ports?this._renderProgress("Loading serial devices"):0===this._ports.length?this._renderMessage("👀","No serial devices found.",!0):d`
              ${this._ports.map((t=>d`
                  <mwc-list-item
                    twoline
                    hasMeta
                    .port=${t.port}
                    @click=${this._handleLegacyOption}
                  >
                    <span>${t.desc}</span>
                    <span slot="secondary">${t.port}</span>
                    ${u}
                  </mwc-list-item>
                `))}

              <mwc-button
                no-attention
                slot="primaryAction"
                label="Back"
                @click=${()=>{this._state="pick_option"}}
              ></mwc-button>
            `):"web_instructions"===this._state&&(t="Install ESPHome via the browser",e=d`
        <p>
          ESPHome can install ${this.configuration} on your device via the
          browser if certain requirements are met:
        </p>
        <ul>
          <li>ESPHome is visited over HTTPS</li>
          <li>Your browser supports WebSerial</li>
        </ul>
        <p>
          Not all requirements are currently met. The easiest solution is to
          download your project and do the installation with ESPHome Web.
          ESPHome Web works 100% in your browser and no data will be shared with
          the ESPHome project.
        </p>
        <ol>
          <li>
            ${y(this._compileConfiguration,d`<a download disabled href="#">Download project</a> preparing
                download…
                <mwc-circular-progress
                  density="-8"
                  indeterminate
                ></mwc-circular-progress>`)}
          </li>
          <li>
            <a href=${"https://web.esphome.io/?dashboard_install"} target="_blank" rel="noopener"
              >Open ESPHome Web</a
            >
          </li>
        </ol>

        <mwc-button
          no-attention
          slot="secondaryAction"
          label="Back"
          @click=${()=>{this._state="pick_option"}}
        ></mwc-button>
      `),d`
      <mwc-dialog
        open
        heading=${t}
        scrimClickAction
        @closed=${this._handleClose}
        .hideActions=${!1}
      >
        ${e}
      </mwc-dialog>
    `}_renderProgress(t,e){return d`
      <div class="center">
        <div>
          <mwc-circular-progress
            active
            ?indeterminate=${void 0===e}
            .progress=${void 0!==e?e/100:void 0}
            density="8"
          ></mwc-circular-progress>
          ${void 0!==e?d`<div class="progress-pct">${e}%</div>`:""}
        </div>
        ${t}
      </div>
    `}_renderMessage(t,e,o){return d`
      <div class="center">
        <div class="icon">${t}</div>
        ${e}
      </div>
      ${o&&d`
        <mwc-button
          slot="primaryAction"
          dialogAction="ok"
          label="Close"
        ></mwc-button>
      `}
    `}firstUpdated(t){super.firstUpdated(t),this._updateSerialPorts()}async _updateSerialPorts(){this._ports=await p()}willUpdate(t){super.willUpdate(t),t.has("_state")&&"web_instructions"===this._state&&!this._compileConfiguration&&(this._abortCompilation=new AbortController,this._compileConfiguration=g(this.configuration).then((()=>d`
            <a download href="${v(this.configuration,!0)}"
              >Download project</a
            >
          `),(()=>d`
            <a download disabled href="#">Download project</a>
            <span class="prepare-error">preparation failed:</span>
            <button
              class="link"
              dialogAction="close"
              @click=${this._handleWebDownload}
            >
              see what went wrong
            </button>
          `)).finally((()=>{this._abortCompilation=void 0})))}updated(t){if(super.updated(t),t.has("_state"))if("pick_server_port"===this._state){const t=async()=>{await this._updateSerialPorts(),this._updateSerialInterval=window.setTimeout((async()=>{await t()}),5e3)};t()}else"pick_server_port"===t.get("_state")&&(clearTimeout(this._updateSerialInterval),this._updateSerialInterval=void 0)}_storeDialogWidth(){this.style.setProperty("--mdc-dialog-min-width",`${this.shadowRoot.querySelector("mwc-list-item").clientWidth+4}px`)}_showServerPorts(){this._storeDialogWidth(),this._state="pick_server_port"}_handleManualDownload(){k(this.configuration,!1)}_handleWebDownload(){k(this.configuration,!0)}_handleLegacyOption(t){C(this.configuration,t.currentTarget.port),this._close()}_handleBrowserInstall(){if(!_||!w)return this._storeDialogWidth(),void(this._state="web_instructions");P({configuration:this.configuration},(()=>this._close()))}_close(){this.shadowRoot.querySelector("mwc-dialog").close()}async _handleClose(){var t;null===(t=this._abortCompilation)||void 0===t||t.abort(),this._updateSerialInterval&&(clearTimeout(this._updateSerialInterval),this._updateSerialInterval=void 0),this.parentNode.removeChild(this)}};x.styles=s`
    a {
      color: var(--mdc-theme-primary);
    }
    mwc-button[no-attention] {
      --mdc-theme-primary: #444;
      --mdc-theme-on-primary: white;
    }
    mwc-list-item {
      margin: 0 -20px;
    }
    svg {
      fill: currentColor;
    }
    .center {
      text-align: center;
    }
    mwc-circular-progress {
      margin-bottom: 16px;
    }
    li mwc-circular-progress {
      margin: 0;
    }
    .progress-pct {
      position: absolute;
      top: 50px;
      left: 0;
      right: 0;
    }
    .icon {
      font-size: 50px;
      line-height: 80px;
      color: black;
    }
    .show-ports {
      margin-top: 16px;
    }
    .error {
      padding: 8px 24px;
      background-color: #fff59d;
      margin: 0 -24px;
    }
    .prepare-error {
      color: var(--alert-error-color);
    }
    li a {
      display: inline-block;
      margin-right: 8px;
    }
    a[disabled] {
      pointer-events: none;
      color: #999;
    }
    button.link {
      background: none;
      color: var(--mdc-theme-primary);
      border: none;
      padding: 0;
      font: inherit;
      text-align: left;
      text-decoration: underline;
      cursor: pointer;
    }
  `,r([a()],x.prototype,"configuration",void 0),r([n()],x.prototype,"_ports",void 0),r([n()],x.prototype,"_state",void 0),r([n()],x.prototype,"_error",void 0),x=r([c("esphome-install-choose-dialog")],x);var j=Object.freeze({__proto__:null});export{k as a,P as b,j as i,C as o};

import{s as t,$ as e,r,_ as i,a as o,c as s,n as a}from"./index-5e3d0838.js";import"./c.5bab727a.js";import"./c.fecaa79b.js";import{a as n,c}from"./c.1e7f773d.js";import{f as l,g as d}from"./c.33c5fa67.js";import{a as h,b as p}from"./c.c63a1677.js";import{_ as m}from"./c.92b39d00.js";import"./c.6a7f81e8.js";let g=class extends t{constructor(){super(...arguments),this._state="connecting_webserial"}render(){let t,r=!1;return"connecting_webserial"===this._state?(t=this._renderProgress("Connecting"),r=!0):"prepare_installation"===this._state?(t=this._renderProgress("Preparing installation"),r=!0):"installing"===this._state?(t=void 0===this._writeProgress?this._renderProgress("Erasing"):this._renderProgress(e`
                Installing<br /><br />
                This will take
                ${"ESP8266"===this._platform?"a minute":"2 minutes"}.<br />
                Keep this page visible to prevent slow down
              `,this._writeProgress>3?this._writeProgress:void 0),r=!0):"done"===this._state&&(t=this._error?t=e`
          ${this._renderMessage("👀",this._error,!1)}
          <mwc-button
            slot="secondaryAction"
            dialogAction="ok"
            label="Close"
          ></mwc-button>
          <mwc-button
            slot="primaryAction"
            label="Retry"
            @click=${this._handleRetry}
          ></mwc-button>
        `:this._renderMessage("🎉","Configuration installed!",!0)),e`
      <mwc-dialog
        open
        heading=${undefined}
        scrimClickAction
        @closed=${this._handleClose}
        .hideActions=${r}
      >
        ${t}
      </mwc-dialog>
    `}_renderProgress(t,r){return e`
      <div class="center">
        <div>
          <mwc-circular-progress
            active
            ?indeterminate=${void 0===r}
            .progress=${void 0!==r?r/100:void 0}
            density="8"
          ></mwc-circular-progress>
          ${void 0!==r?e`<div class="progress-pct">${r}%</div>`:""}
        </div>
        ${t}
      </div>
    `}_renderMessage(t,r,i){return e`
      <div class="center">
        <div class="icon">${t}</div>
        ${r}
      </div>
      ${i?e`
            <mwc-button
              slot="primaryAction"
              dialogAction="ok"
              label="Close"
            ></mwc-button>
          `:""}
    `}firstUpdated(t){super.firstUpdated(t),this._handleInstall()}_showCompileDialog(){h(this.params.configuration,!1),this._close()}_handleRetry(){p(this.params,(()=>this._close()))}async _handleInstall(){const t=this.esploader;t.port.addEventListener("disconnect",(async()=>{this._state="done",this._error="Device disconnected",this.params.port||await t.port.close()}));try{try{await t.initialize()}catch(e){return console.error(e),this._state="done",this._error="Failed to initialize.",void(t.connected&&(this._error+=" Try resetting your device or holding the BOOT button while selecting your serial port until it starts preparing the installation."))}this._platform=m[t.chipFamily];const e=this.params.filesCallback||(t=>this._getFilesForConfiguration(this.params.configuration,t));let r=[];try{r=await e(this._platform)}catch(t){return this._state="done",void(this._error=String(t))}if(!r)return;this._state="installing";try{await l(t,r,!0===this.params.erase,(t=>{this._writeProgress=t}))}catch(t){return void("done"!==this._state&&(this._error=`Installation failed: ${t}`,this._state="done"))}await t.hardReset(),this._state="done"}finally{if(t.connected&&(console.log("Disconnecting esp"),await t.disconnect()),!this.params.port){console.log("Closing port");try{await t.port.close()}catch(t){}}}}async _getFilesForConfiguration(t,r){let i;try{i=await n(t)}catch(t){return this._state="done",void(this._error="Error fetching configuration information")}if(r!==i.esp_platform.toUpperCase())return this._state="done",void(this._error=`Configuration does not match the platform of the connected device. Expected an ${i.esp_platform.toUpperCase()} device.`);this._state="prepare_installation";try{await c(t)}catch(t){return this._error=e`
        Failed to prepare configuration<br /><br />
        <button class="link" @click=${this._showCompileDialog}>
          See what went wrong.
        </button>
      `,void(this._state="done")}return"done"!==this._state?await d(t):void 0}_close(){this.shadowRoot.querySelector("mwc-dialog").close()}async _handleClose(){this.params.onClose&&this.params.onClose("done"===this._state&&void 0===this._error),this.parentNode.removeChild(this)}};g.styles=r`
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
    .show-ports {
      margin-top: 16px;
    }
    .error {
      padding: 8px 24px;
      background-color: #fff59d;
      margin: 0 -24px;
    }
  `,i([o()],g.prototype,"params",void 0),i([o()],g.prototype,"esploader",void 0),i([s()],g.prototype,"_writeProgress",void 0),i([s()],g.prototype,"_state",void 0),i([s()],g.prototype,"_error",void 0),g=i([a("esphome-install-web-dialog")],g);export{g as ESPHomeInstallWebDialog};

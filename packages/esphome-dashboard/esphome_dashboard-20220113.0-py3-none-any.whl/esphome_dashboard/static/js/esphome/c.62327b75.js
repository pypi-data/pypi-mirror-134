import{r as t,_ as e,a as o,c as s,n as i,s as r,$ as a}from"./index-5e3d0838.js";import"./c.5bab727a.js";import"./c.98b47311.js";import{g as n}from"./c.6a7f81e8.js";import{m as c,s as l,a as p}from"./c.92b39d00.js";const m=(t,e)=>{import("./c.97c545d0.js");const o=document.createElement("esphome-logs-dialog");o.configuration=t,o.target=e,document.body.append(o)},h=(t,e)=>{import("./c.f08a4e92.js");const o=document.createElement("esphome-logs-webserial-dialog");o.configuration=e,o.port=t,document.body.append(o)};let d=class extends r{constructor(){super(...arguments),this._show="options"}render(){let t,e;return"options"===this._show?(t="How to get the logs for your ESP device?",e=a`
        <mwc-list-item
          twoline
          hasMeta
          dialogAction="close"
          .port=${"OTA"}
          @click=${this._pickPort}
        >
          <span>Wirelessly</span>
          <span slot="secondary">Requires the device to be online</span>
          ${c}
        </mwc-list-item>

        <mwc-list-item
          twoline
          hasMeta
          .port=${"WEBSERIAL"}
          @click=${this._pickWebSerial}
        >
          <span>Plug into this computer</span>
          <span slot="secondary">
            For devices connected via USB to this computer
          </span>
          ${c}
        </mwc-list-item>

        <mwc-list-item twoline hasMeta @click=${this._showServerPorts}>
          <span>Plug into the computer running ESPHome Dashboard</span>
          <span slot="secondary">
            For devices connected via USB to the server
          </span>
          ${c}
        </mwc-list-item>
      `):"web_instructions"===this._show?(t="View logs in the browser",e=a`
        <p>
          ESPHome can view the logs of your device via the browser if certain
          requirements are met:
        </p>
        <ul>
          <li>ESPHome is visited over HTTPS</li>
          <li>Your browser supports WebSerial</li>
        </ul>
        <p>
          Not all requirements are currently met. The easiest solution is to
          view the logs with ESPHome Web. ESPHome Web works 100% in your browser
          and no data will be shared with the ESPHome project.
        </p>

        <a
          slot="primaryAction"
          href=${"https://web.esphome.io/?dashboard_logs"}
          target="_blank"
          rel="noopener"
        >
          <mwc-button
            dialogAction="close"
            label="OPEN ESPHOME WEB"
          ></mwc-button>
        </a>
      `):(t="Pick server port",e=void 0===this._ports?a`
              <mwc-list-item>
                <span>Loading ports…</span>
              </mwc-list-item>
            `:0===this._ports.length?a`
              <mwc-list-item>
                <span>No serial ports found.</span>
              </mwc-list-item>
            `:this._ports.map((t=>a`
                <mwc-list-item
                  twoline
                  hasMeta
                  dialogAction="close"
                  .port=${t.port}
                  @click=${this._pickPort}
                >
                  <span>${t.desc}</span>
                  <span slot="secondary">${t.port}</span>
                  ${c}
                </mwc-list-item>
              `))),a`
      <mwc-dialog
        open
        heading=${t}
        scrimClickAction
        @closed=${this._handleClose}
      >
        ${e}

        <mwc-button
          no-attention
          slot="secondaryAction"
          dialogAction="close"
          label="Cancel"
        ></mwc-button>
      </mwc-dialog>
    `}firstUpdated(t){super.firstUpdated(t),n().then((t=>{0!==t.length||l?this._ports=t:(this._handleClose(),m(this.configuration,"OTA"))}))}_showServerPorts(){this._show="server_ports"}_pickPort(t){m(this.configuration,t.currentTarget.port)}async _pickWebSerial(t){if(l&&p)try{const t=await navigator.serial.requestPort();await t.open({baudRate:115200}),this.shadowRoot.querySelector("mwc-dialog").close(),h(t,this.configuration)}catch(t){console.error(t)}else this._show="web_instructions"}_handleClose(){this.parentNode.removeChild(this)}};d.styles=t`
    mwc-list-item {
      margin: 0 -20px;
    }

    mwc-button[no-attention] {
      --mdc-theme-primary: #444;
      --mdc-theme-on-primary: white;
    }
  `,e([o()],d.prototype,"configuration",void 0),e([s()],d.prototype,"_ports",void 0),e([s()],d.prototype,"_show",void 0),d=e([i("esphome-logs-target-dialog")],d);var w=Object.freeze({__proto__:null});export{w as l,m as o};

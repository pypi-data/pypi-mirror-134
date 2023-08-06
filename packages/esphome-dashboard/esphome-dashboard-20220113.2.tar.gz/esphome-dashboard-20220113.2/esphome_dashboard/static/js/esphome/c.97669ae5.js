import{r as o,_ as t,c as e,f as i,n as a,s as r,$ as s}from"./index-7c1fc97a.js";import"./c.da084acf.js";import{a as n}from"./c.d40ca3f3.js";import{g as c}from"./c.e3657a72.js";import"./c.c146edc1.js";import"./c.1aae5b08.js";import"./c.69ebd33d.js";import"./c.c5564c7b.js";let d=class extends r{constructor(){super(...arguments),this.downloadFactoryFirmware=!0}render(){return s`
      <esphome-process-dialog
        .heading=${`Download ${this.configuration}`}
        .type=${"compile"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        ${void 0===this._result?"":0===this._result?s`
              <a
                slot="secondaryAction"
                href="${c(this.configuration,this.downloadFactoryFirmware)}"
              >
                <mwc-button label="Download"></mwc-button>
              </a>
            `:s`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_handleProcessDone(o){if(this._result=o.detail,0!==o.detail)return;const t=document.createElement("a");t.download=this.configuration+".bin",t.href=c(this.configuration,this.downloadFactoryFirmware),document.body.appendChild(t),t.click(),t.remove()}_handleRetry(){n(this.configuration,this.downloadFactoryFirmware)}_handleClose(){this.parentNode.removeChild(this)}};d.styles=o`
    a {
      text-decoration: none;
    }
  `,t([e()],d.prototype,"configuration",void 0),t([e()],d.prototype,"downloadFactoryFirmware",void 0),t([i()],d.prototype,"_result",void 0),d=t([a("esphome-compile-dialog")],d);

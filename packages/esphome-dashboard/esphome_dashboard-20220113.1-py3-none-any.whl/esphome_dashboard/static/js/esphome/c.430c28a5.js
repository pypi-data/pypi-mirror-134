import{r as o,_ as e,a as t,c as i,n as a,s as r,$ as s}from"./index-acc71b99.js";import"./c.195e6e9d.js";import{a as n}from"./c.79a9be70.js";import{g as c}from"./c.a0f0ec15.js";import"./c.6aeb6c9e.js";import"./c.75023507.js";import"./c.9b8e48ba.js";import"./c.0ba40d5f.js";let d=class extends r{constructor(){super(...arguments),this.downloadFactoryFirmware=!0}render(){return s`
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
    `}_handleProcessDone(o){if(this._result=o.detail,0!==o.detail)return;const e=document.createElement("a");e.download=this.configuration+".bin",e.href=c(this.configuration,this.downloadFactoryFirmware),document.body.appendChild(e),e.click(),e.remove()}_handleRetry(){n(this.configuration,this.downloadFactoryFirmware)}_handleClose(){this.parentNode.removeChild(this)}};d.styles=o`
    a {
      text-decoration: none;
    }
  `,e([t()],d.prototype,"configuration",void 0),e([t()],d.prototype,"downloadFactoryFirmware",void 0),e([i()],d.prototype,"_result",void 0),d=e([a("esphome-compile-dialog")],d);

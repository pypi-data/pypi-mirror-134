import{_ as o,a as t,c as e,n as s,s as i,$ as a,P as r}from"./index-acc71b99.js";import"./c.195e6e9d.js";import{o as n}from"./c.52997d0d.js";import"./c.6aeb6c9e.js";import"./c.75023507.js";import"./c.0ba40d5f.js";let c=class extends i{render(){return a`
      <esphome-process-dialog
        always-show-close
        .heading=${`Logs ${this.configuration}`}
        .type=${"logs"}
        .spawnParams=${{configuration:this.configuration,port:this.target}}
        @closed=${this._handleClose}
        @process-done=${this._handleProcessDone}
      >
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Edit"
          @click=${this._openEdit}
        ></mwc-button>
        ${void 0===this._result||0===this._result?"":a`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_openEdit(){r(this.configuration)}_handleProcessDone(o){this._result=o.detail}_handleRetry(){n(this.configuration,this.target)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],c.prototype,"configuration",void 0),o([t()],c.prototype,"target",void 0),o([e()],c.prototype,"_result",void 0),c=o([s("esphome-logs-dialog")],c);

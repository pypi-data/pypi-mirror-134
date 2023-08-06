import{_ as o,c as t,f as s,n as e,s as i,$ as r,Q as a}from"./index-9546641d.js";import"./c.011c3565.js";import{o as n}from"./c.13b217ff.js";import"./c.4281a888.js";import"./c.b72e0f20.js";import"./c.4dab1567.js";let c=class extends i{render(){return r`
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
        ${void 0===this._result||0===this._result?"":r`
              <mwc-button
                slot="secondaryAction"
                dialogAction="close"
                label="Retry"
                @click=${this._handleRetry}
              ></mwc-button>
            `}
      </esphome-process-dialog>
    `}_openEdit(){a(this.configuration)}_handleProcessDone(o){this._result=o.detail}_handleRetry(){n(this.configuration,this.target)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],c.prototype,"configuration",void 0),o([t()],c.prototype,"target",void 0),o([s()],c.prototype,"_result",void 0),c=o([e("esphome-logs-dialog")],c);

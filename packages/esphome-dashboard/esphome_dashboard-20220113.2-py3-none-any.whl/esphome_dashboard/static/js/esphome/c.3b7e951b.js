import{_ as o,c as t,f as s,n as e,s as i,$ as a,Q as c}from"./index-7c1fc97a.js";import"./c.da084acf.js";import{o as r}from"./c.767f8316.js";import"./c.c146edc1.js";import"./c.1aae5b08.js";import"./c.c5564c7b.js";let n=class extends i{render(){return a`
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
    `}_openEdit(){c(this.configuration)}_handleProcessDone(o){this._result=o.detail}_handleRetry(){r(this.configuration,this.target)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],n.prototype,"configuration",void 0),o([t()],n.prototype,"target",void 0),o([s()],n.prototype,"_result",void 0),n=o([e("esphome-logs-dialog")],n);

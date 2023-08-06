import{_ as o,a as t,n as e,s as i,$ as n,P as s,C as a}from"./index-acc71b99.js";import"./c.195e6e9d.js";import"./c.6aeb6c9e.js";let c=class extends i{render(){return n`
      <esphome-process-dialog
        .heading=${`Clean ${this.configuration}`}
        .type=${"clean"}
        .spawnParams=${{configuration:this.configuration}}
        @closed=${this._handleClose}
      >
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Edit"
          @click=${this._openEdit}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          dialogAction="close"
          label="Install"
          @click=${this._openInstall}
        ></mwc-button>
      </esphome-process-dialog>
    `}_openEdit(){s(this.configuration)}_openInstall(){a(this.configuration)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],c.prototype,"configuration",void 0),c=o([e("esphome-clean-dialog")],c);

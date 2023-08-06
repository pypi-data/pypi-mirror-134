import{_ as o,c as t,n as i,s as n,$ as e,Q as s,D as a}from"./index-9546641d.js";import"./c.011c3565.js";import"./c.4281a888.js";let c=class extends n{render(){return e`
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
    `}_openEdit(){s(this.configuration)}_openInstall(){a(this.configuration)}_handleClose(){this.parentNode.removeChild(this)}};o([t()],c.prototype,"configuration",void 0),c=o([i("esphome-clean-dialog")],c);

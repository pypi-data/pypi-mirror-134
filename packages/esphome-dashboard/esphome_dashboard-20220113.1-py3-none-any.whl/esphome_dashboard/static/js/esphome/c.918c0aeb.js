import{_ as e,a as t,n as o,s as a,$ as i,O as l}from"./index-acc71b99.js";import"./c.6aeb6c9e.js";import{d as n}from"./c.a0f0ec15.js";let c=class extends a{render(){return i`
      <mwc-dialog
        .heading=${`Delete ${this.name}`}
        @closed=${this._handleClose}
        open
      >
        <div>Are you sure you want to delete ${this.name}?</div>
        <mwc-button
          slot="primaryAction"
          label="Delete"
          dialogAction="close"
          @click=${this._handleDelete}
        ></mwc-button>
        <mwc-button
          slot="secondaryAction"
          label="Cancel"
          dialogAction="cancel"
        ></mwc-button>
      </mwc-dialog>
    `}_handleClose(){this.parentNode.removeChild(this)}async _handleDelete(){await n(this.configuration),l(this,"deleted")}};e([t()],c.prototype,"name",void 0),e([t()],c.prototype,"configuration",void 0),c=e([o("esphome-delete-device-dialog")],c);

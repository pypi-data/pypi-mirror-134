import{r as e,_ as t,n as o,s as i,$ as r}from"./index-5e3d0838.js";import"./c.5bab727a.js";import"./c.fecaa79b.js";import"./c.92b39d00.js";let s=class extends i{render(){return r`
      <mwc-dialog
        open
        heading="No port selected"
        scrimClickAction
        @closed=${this._handleClose}
      >
        <p>
          If you didn't select a port because you didn't see your device listed,
          try the following steps:
        </p>
        <ol>
          <li>
            Make sure that the device is connected to this computer (the one
            that runs the browser that shows this website)
          </li>
          <li>
            Most devices have a tiny light when it is powered on. Make sure it
            is on.
          </li>
          <li>
            Make sure you have the right drivers installed. Below are the
            drivers for common chips used in ESP devices:
            <ul>
              <li>
                CP2102 (square chip):
                <a
                  href="https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers"
                  target="_blank"
                  rel="noopener"
                  >driver</a
                >
              </li>
              <li>
                CH341:
                <a
                  href="https://github.com/nodemcu/nodemcu-devkit/tree/master/Drivers"
                  target="_blank"
                  rel="noopener"
                  >driver</a
                >
              </li>
            </ul>
          </li>
        </ol>
        ${this.doTryAgain?r`
              <mwc-button
                slot="primaryAction"
                dialogAction="close"
                label="Try Again"
                @click=${this.doTryAgain}
              ></mwc-button>

              <mwc-button
                no-attention
                slot="secondaryAction"
                dialogAction="close"
                label="Cancel"
              ></mwc-button>
            `:r`
              <mwc-button
                slot="primaryAction"
                dialogAction="close"
                label="Close"
              ></mwc-button>
            `}
      </mwc-dialog>
    `}async _handleClose(){this.parentNode.removeChild(this)}};s.styles=e`
    a {
      color: var(--mdc-theme-primary);
    }
    mwc-button[no-attention] {
      --mdc-theme-primary: #444;
      --mdc-theme-on-primary: white;
    }
    li + li,
    li > ul {
      margin-top: 8px;
    }
  `,s=t([o("esphome-no-port-picked-dialog")],s);

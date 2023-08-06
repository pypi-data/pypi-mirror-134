function h(unsafe) {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

class TabbedStructBlockValidationError {
  constructor(blockErrors) {
    this.blockErrors = blockErrors;
  }
}

class TabbedStructBlock {
  constructor(blockDef, placeholder, prefix, initialState, initialError) {
    const state = initialState || {};
    this.blockDef = blockDef;
    this.type = blockDef.name;
    this.childBlocks = {};
    console.log(state);

    const namespace = h(this.blockDef.meta.classname || "");
    const dom = $(`
        <div id="${namespace}" class="tabbed-struct ${namespace}">
        </div>
      `);
    $(placeholder).replaceWith(dom);
    const tabs = $(`
        <ul>
        </ul>
      `);
    blockDef.meta.panels.forEach((p, idx) => {
      let ns = `${namespace}-tab-${p.handle}`;
      tabs.append(`<li>
                <a href="#${ns}-content">${p.label}</a>
            </li>
        `);
      let tab = $(
        `<section id="${ns}-content" class="${p.classnames}"></section>`
      );
      dom.append(tab);
      p.fields.forEach((field, idx) => {
        const childBlockDef = this.blockDef.childBlockDefs.find(
          (c) => c.name == field.field
        );
        const label = field.hide_label
          ? ""
          : `<label class="field__label">${h(
              childBlockDef.meta.label
            )}</label>`;
        const childDom = $(`
          <div class="field ${childBlockDef.meta.required ? "required" : ""} ${
          field.classnames
        }" data-contentpath="${childBlockDef.name}">
            ${label}
            <div data-streamfield-block></div>
          </div>
        `);
        tab.append(childDom);
        const childBlockElement = childDom
          .find("[data-streamfield-block]")
          .get(0);

        const childBlock = childBlockDef.render(
          childBlockElement,
          prefix + "-" + childBlockDef.name,
          state[childBlockDef.name],
          initialError?.blockErrors[childBlockDef.name]
        );
        this.childBlocks[childBlockDef.name] = childBlock;
        if (!field.hide_label) {
          const labelElement = childDom.find("label").get(0);
          if (childBlock.idForLabel) {
            labelElement.setAttribute("for", childBlock.idForLabel);
          }
        }
      });

      if (idx == 0) {
        tabs.attr("data-current-tab", ns);
      }
    });
    if (this.blockDef.meta.helpText) {
      // help text is left unescaped as per Django conventions
      dom.prepend(`
          <span>
            <div class="help">
              ${this.blockDef.meta.helpIcon}
              ${this.blockDef.meta.helpText}
            </div>
          </span>
        `);
    }
    dom.prepend(tabs);
    $(`#${namespace}`).tabs();
  }

  setState(state) {
    // eslint-disable-next-line guard-for-in, no-restricted-syntax
    for (const name in state) {
      this.childBlocks[name].setState(state[name]);
    }
  }

  setError(errorList) {
    if (errorList.length !== 1) {
      return;
    }
    const error = errorList[0];

    // eslint-disable-next-line no-restricted-syntax
    for (const blockName in error.blockErrors) {
      if (error.blockErrors.hasOwnProperty(blockName)) {
        this.childBlocks[blockName].setError(error.blockErrors[blockName]);
      }
    }
  }

  getState() {
    const state = {};
    // eslint-disable-next-line guard-for-in, no-restricted-syntax
    for (const name in this.childBlocks) {
      state[name] = this.childBlocks[name].getState();
    }
    return state;
  }

  getValue() {
    const value = {};
    // eslint-disable-next-line guard-for-in, no-restricted-syntax
    for (const name in this.childBlocks) {
      value[name] = this.childBlocks[name].getValue();
    }
    return value;
  }

  getTextLabel(opts) {
    if (this.blockDef.meta.labelFormat) {
      return this.blockDef.meta.labelFormat.replace(
        /\{(\w+)\}/g,
        (tag, blockName) => {
          const block = this.childBlocks[blockName];
          if (block.getTextLabel) {
            return block.getTextLabel(opts);
          }
          return "";
        }
      );
    }

    /* if no labelFormat specified, just try each child block in turn until we find one that provides a label */
    for (const childDef of this.blockDef.childBlockDefs) {
      const child = this.childBlocks[childDef.name];
      if (child.getTextLabel) {
        const val = child.getTextLabel(opts);
        if (val) return val;
      }
    }
    // no usable label found
    return null;
  }

  focus(opts) {
    if (this.blockDef.childBlockDefs.length) {
      const firstChildName = this.blockDef.childBlockDefs[0].name;
      this.childBlocks[firstChildName].focus(opts);
    }
  }
}

class TabbedStructBlockDefinition extends window.wagtailStreamField.blocks
  .StructBlockDefinition {
  render(placeholder, prefix, initialState, initialError) {
    return new TabbedStructBlock(
      this,
      placeholder,
      prefix,
      initialState,
      initialError
    );
  }
}

window.telepath.register(
  "pages.blocks.TabbedStructBlock",
  TabbedStructBlockDefinition
);

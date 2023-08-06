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

    const namespace = h(this.blockDef.meta.classname || "");
    const dom = $(`
        <div id="${namespace}" class="collapsable-struct ${namespace}">
        </div>
      `);
    $(placeholder).replaceWith(dom);
    if (this.blockDef.meta.helpText) {
      // help text is left unescaped as per Django conventions
      dom.append(`
          <span>
            <div class="help">
              ${this.blockDef.meta.helpIcon}
              ${this.blockDef.meta.helpText}
            </div>
          </span>
        `);
    }
    this.blockDef.childBlockDefs
      .filter((c) => this.blockDef.meta.collapsible.indexOf(c) == -1)
      .forEach((childBlockDef, idx) => {
        const childDom = $(`
          <div class="field ${
            childBlockDef.meta.required ? "required" : ""
          }" data-contentpath="${childBlockDef.name}">
            <label class="field__label">${h(childBlockDef.meta.label)}</label>
            <div data-streamfield-block></div>
          </div>
        `);
        dom.append(childDom);
        const childBlockElement = childDom
          .find("[data-streamfield-block]")
          .get(0);
        const labelElement = childDom.find("label").get(0);
        const childBlock = childBlockDef.render(
          childBlockElement,
          prefix + "-" + childBlockDef.name,
          state[childBlockDef.name],
          initialError?.blockErrors[childBlockDef.name]
        );

        this.childBlocks[childBlockDef.name] = childBlock;
        if (childBlock.idForLabel) {
          labelElement.setAttribute("for", childBlock.idForLabel);
        }
      });
    if (this.blockDef.meta.collapsible.length > 0) {
      const c_section = $(
        `<section id="${namespace}-collapsible-section" class="collapsible-section"></section>`
      );
      dom.append(c_section);
      this.blockDef.childBlockDefs
        .filter((c) => this.blockDef.meta.collapsible.indexOf(c) >= 0)
        .forEach((childBlockDef, idx) => {
          const childDom = $(`
          <div class="field ${
            childBlockDef.meta.required ? "required" : ""
          }" data-contentpath="${childBlockDef.name}">
            <label class="field__label">${h(childBlockDef.meta.label)}</label>
            <div data-streamfield-block></div>
          </div>
        `);
          dom.append(childDom);
          const childBlockElement = childDom
            .find("[data-streamfield-block]")
            .get(0);
          const labelElement = childDom.find("label").get(0);
          const childBlock = childBlockDef.render(
            childBlockElement,
            prefix + "-" + childBlockDef.name,
            state[childBlockDef.name],
            initialError?.blockErrors[childBlockDef.name]
          );

          this.childBlocks[childBlockDef.name] = childBlock;
          if (childBlock.idForLabel) {
            labelElement.setAttribute("for", childBlock.idForLabel);
          }
        });
    }
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

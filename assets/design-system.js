/* @ds-bundle: {"format":4,"namespace":"MickaelTeixeiraDesignSystem_e955b5","components":[{"name":"Button","sourcePath":"components/actions/Button.jsx"},{"name":"IconButton","sourcePath":"components/actions/IconButton.jsx"},{"name":"Badge","sourcePath":"components/display/Badge.jsx"},{"name":"Card","sourcePath":"components/display/Card.jsx"},{"name":"Tabs","sourcePath":"components/display/Tabs.jsx"},{"name":"Tag","sourcePath":"components/display/Tag.jsx"},{"name":"Checkbox","sourcePath":"components/forms/Checkbox.jsx"},{"name":"Input","sourcePath":"components/forms/Input.jsx"},{"name":"Select","sourcePath":"components/forms/Select.jsx"},{"name":"Switch","sourcePath":"components/forms/Switch.jsx"},{"name":"Textarea","sourcePath":"components/forms/Textarea.jsx"},{"name":"Barcode","sourcePath":"components/motifs/Barcode.jsx"},{"name":"DitherImage","sourcePath":"components/motifs/DitherImage.jsx"},{"name":"Globe","sourcePath":"components/motifs/Globe.jsx"},{"name":"HazardTape","sourcePath":"components/motifs/HazardTape.jsx"},{"name":"Starburst","sourcePath":"components/motifs/Starburst.jsx"},{"name":"WarpGrid","sourcePath":"components/motifs/WarpGrid.jsx"},{"name":"Footer","sourcePath":"components/site/Footer.jsx"},{"name":"ProjectCard","sourcePath":"components/site/ProjectCard.jsx"},{"name":"SiteNav","sourcePath":"components/site/SiteNav.jsx"},{"name":"Marquee","sourcePath":"components/typography/Marquee.jsx"},{"name":"MetaTable","sourcePath":"components/typography/MetaTable.jsx"},{"name":"SectionHeader","sourcePath":"components/typography/SectionHeader.jsx"},{"name":"AboutScreen","sourcePath":"ui_kits/portfolio/AboutScreen.jsx"},{"name":"HomeScreen","sourcePath":"ui_kits/portfolio/HomeScreen.jsx"},{"name":"ProjectScreen","sourcePath":"ui_kits/portfolio/ProjectScreen.jsx"}],"sourceHashes":{"components/actions/Button.jsx":"d1492dc206f9","components/actions/IconButton.jsx":"4683c5760d97","components/display/Badge.jsx":"8a09c573d9e5","components/display/Card.jsx":"2770cc25a73e","components/display/Tabs.jsx":"1f0986cabf27","components/display/Tag.jsx":"a3d11c95a483","components/forms/Checkbox.jsx":"69c00158b43e","components/forms/Input.jsx":"4b093cd2f00d","components/forms/Select.jsx":"57da7266e6e7","components/forms/Switch.jsx":"3566aef46c0f","components/forms/Textarea.jsx":"254b3ac7aa2e","components/motifs/Barcode.jsx":"0f7d70fcc142","components/motifs/DitherImage.jsx":"308d6a8c6a3b","components/motifs/Globe.jsx":"a8f0f345f5fa","components/motifs/HazardTape.jsx":"0ccf8ea8795c","components/motifs/Starburst.jsx":"09b146aca955","components/motifs/WarpGrid.jsx":"bed7364a0b3f","components/site/Footer.jsx":"04beac90a3b6","components/site/ProjectCard.jsx":"d4bd0a106cf2","components/site/SiteNav.jsx":"3ef03c4edc01","components/typography/Marquee.jsx":"93905e6fdecf","components/typography/MetaTable.jsx":"9d0baf1e76b7","components/typography/SectionHeader.jsx":"dc6a717abbea","ui_kits/portfolio/AboutScreen.jsx":"3cc831e41809","ui_kits/portfolio/HomeScreen.jsx":"75641b031c3c","ui_kits/portfolio/ProjectScreen.jsx":"1f3b4909ad07"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.MickaelTeixeiraDesignSystem_e955b5 = window.MickaelTeixeiraDesignSystem_e955b5 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/actions/Button.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-family:var(--font-mono);text-transform:uppercase;letter-spacing:var(--tracking-caps);font-weight:500;border-radius:var(--radius-pill);border:1px solid transparent;cursor:pointer;white-space:nowrap;text-decoration:none;user-select:none;transition:background var(--duration-fast) var(--ease-mech),color var(--duration-fast) var(--ease-mech),border-color var(--duration-fast) var(--ease-mech)}
.mt-btn:active{transform:translate(1px,1px)}
.mt-btn[data-size="sm"]{height:28px;padding:0 14px;font-size:10.5px}
.mt-btn[data-size="md"]{height:36px;padding:0 18px;font-size:11.5px}
.mt-btn[data-size="lg"]{height:46px;padding:0 26px;font-size:12.5px}
.mt-btn[data-variant="primary"]{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-btn[data-variant="primary"]:hover{background:transparent;color:var(--text-primary)}
.mt-btn[data-variant="accent"]{background:var(--accent);color:#000;border-color:var(--accent)}
.mt-btn[data-variant="accent"]:hover{background:transparent;color:var(--accent)}
.mt-btn[data-variant="outline"]{background:transparent;color:var(--text-primary);border-color:var(--border-strong)}
.mt-btn[data-variant="outline"]:hover{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-btn[data-variant="ghost"]{background:transparent;color:var(--text-secondary);border-color:transparent}
.mt-btn[data-variant="ghost"]:hover{color:var(--link-hover)}
.mt-btn[data-disabled="true"]{opacity:.35;pointer-events:none}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-btn-css')) {
  const s = document.createElement('style');
  s.id = 'mt-btn-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Button({
  variant = 'primary',
  size = 'md',
  disabled = false,
  href,
  arrow = false,
  children,
  style,
  ...rest
}) {
  const Tag = href ? 'a' : 'button';
  return /*#__PURE__*/React.createElement(Tag, _extends({
    className: "mt-btn",
    "data-variant": variant,
    "data-size": size,
    "data-disabled": disabled || undefined,
    disabled: href ? undefined : disabled,
    href: href,
    style: style
  }, rest), children, arrow && /*#__PURE__*/React.createElement("span", {
    "aria-hidden": "true"
  }, "\u2192"));
}
Object.assign(__ds_scope, { Button });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/actions/Button.jsx", error: String((e && e.message) || e) }); }

// components/actions/IconButton.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-iconbtn{display:inline-flex;align-items:center;justify-content:center;background:transparent;color:var(--text-primary);border:1px solid var(--border-strong);cursor:pointer;padding:0;transition:background var(--duration-fast) var(--ease-mech),color var(--duration-fast) var(--ease-mech),border-color var(--duration-fast) var(--ease-mech)}
.mt-iconbtn:hover{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-iconbtn:active{transform:translate(1px,1px)}
.mt-iconbtn[data-shape="circle"]{border-radius:var(--radius-pill)}
.mt-iconbtn[data-shape="square"]{border-radius:var(--radius-0)}
.mt-iconbtn[data-size="sm"]{width:28px;height:28px;font-size:12px}
.mt-iconbtn[data-size="md"]{width:36px;height:36px;font-size:14px}
.mt-iconbtn[data-size="lg"]{width:46px;height:46px;font-size:18px}
.mt-iconbtn[data-disabled="true"]{opacity:.35;pointer-events:none}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-iconbtn-css')) {
  const s = document.createElement('style');
  s.id = 'mt-iconbtn-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function IconButton({
  label,
  shape = 'circle',
  size = 'md',
  disabled = false,
  href,
  children,
  style,
  ...rest
}) {
  const Tag = href ? 'a' : 'button';
  return /*#__PURE__*/React.createElement(Tag, _extends({
    className: "mt-iconbtn",
    "aria-label": label,
    title: label,
    "data-shape": shape,
    "data-size": size,
    "data-disabled": disabled || undefined,
    disabled: href ? undefined : disabled,
    href: href,
    style: style
  }, rest), children);
}
Object.assign(__ds_scope, { IconButton });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/actions/IconButton.jsx", error: String((e && e.message) || e) }); }

// components/display/Badge.jsx
try { (() => {
const css = `
.mt-badge{display:inline-flex;align-items:center;gap:8px;height:24px;padding:0 12px;border:1px solid var(--border-strong);border-radius:var(--radius-pill);font:500 10.5px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-primary);white-space:nowrap}
.mt-badge[data-filled="true"]{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-badge-dot{width:6px;height:6px;border-radius:50%;flex:none}
.mt-badge-dot[data-live="true"]{animation:mt-badge-blink 1.2s steps(2,end) infinite}
@keyframes mt-badge-blink{50%{opacity:.15}}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-badge-css')) {
  const s = document.createElement('style');
  s.id = 'mt-badge-css';
  s.textContent = css;
  document.head.appendChild(s);
}
const TONES = {
  neutral: 'currentColor',
  positive: 'var(--positive)',
  negative: 'var(--negative)',
  warning: 'var(--warning)',
  accent: 'var(--accent)',
  orange: 'var(--accent-2)'
};
function Badge({
  tone = 'neutral',
  dot = true,
  live = false,
  filled = false,
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("span", {
    className: "mt-badge",
    "data-filled": filled || undefined,
    style: style
  }, dot && /*#__PURE__*/React.createElement("span", {
    className: "mt-badge-dot",
    "data-live": live || undefined,
    style: {
      background: TONES[tone] || TONES.neutral
    }
  }), children);
}
Object.assign(__ds_scope, { Badge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Badge.jsx", error: String((e && e.message) || e) }); }

// components/display/Card.jsx
try { (() => {
const css = `
.mt-card{position:relative;border:1px solid var(--border);background:var(--surface-card);transition:border-color var(--duration-fast) var(--ease-out)}
.mt-card[data-hover="true"]:hover{border-color:var(--border-strong)}
[data-theme="light"] .mt-card{box-shadow:var(--shadow-hard)}
.mt-card-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;padding:12px 16px;border-bottom:1px solid var(--border)}
.mt-card-title{font:500 11px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-primary)}
.mt-card-meta{font:400 10.5px var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--text-tertiary)}
.mt-card-body{padding:16px}
.mt-card-tick{position:absolute;font:400 12px/1 var(--font-mono);color:var(--text-secondary);pointer-events:none}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-card-css')) {
  const s = document.createElement('style');
  s.id = 'mt-card-css';
  s.textContent = css;
  document.head.appendChild(s);
}
const TICKS = [{
  top: -7,
  left: -4
}, {
  top: -7,
  right: -4
}, {
  bottom: -7,
  left: -4
}, {
  bottom: -7,
  right: -4
}];
function Card({
  title,
  meta,
  corners = false,
  hover = true,
  padded = true,
  children,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "mt-card",
    "data-hover": hover,
    style: style
  }, corners && TICKS.map((p, i) => /*#__PURE__*/React.createElement("span", {
    key: i,
    className: "mt-card-tick",
    "aria-hidden": "true",
    style: p
  }, "+")), (title || meta) && /*#__PURE__*/React.createElement("div", {
    className: "mt-card-head"
  }, /*#__PURE__*/React.createElement("span", {
    className: "mt-card-title"
  }, title), meta && /*#__PURE__*/React.createElement("span", {
    className: "mt-card-meta"
  }, meta)), padded ? /*#__PURE__*/React.createElement("div", {
    className: "mt-card-body"
  }, children) : children);
}
Object.assign(__ds_scope, { Card });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Card.jsx", error: String((e && e.message) || e) }); }

// components/display/Tabs.jsx
try { (() => {
const {
  useState
} = React;
const css = `
.mt-tabs{display:flex;border-bottom:1px solid var(--border)}
.mt-tab{font:500 11px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;padding:10px 16px;color:var(--text-secondary);background:none;border:0;border-bottom:2px solid transparent;margin-bottom:-1px;cursor:pointer;transition:color var(--duration-fast) var(--ease-out)}
.mt-tab:hover{color:var(--text-primary)}
.mt-tab[data-active="true"]{color:var(--text-primary);border-bottom-color:var(--text-primary)}
.mt-tab-index{color:var(--text-tertiary);margin-right:6px}
.mt-tab-panel{padding:16px 0}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-tabs-css')) {
  const s = document.createElement('style');
  s.id = 'mt-tabs-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Tabs({
  items = [],
  active,
  onChange,
  indexed = true,
  style
}) {
  const [internal, setInternal] = useState(items[0] && items[0].id);
  const current = active !== undefined ? active : internal;
  const activeItem = items.find(i => i.id === current);
  return /*#__PURE__*/React.createElement("div", {
    style: style
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-tabs",
    role: "tablist"
  }, items.map((it, i) => /*#__PURE__*/React.createElement("button", {
    key: it.id,
    role: "tab",
    className: "mt-tab",
    "data-active": it.id === current,
    "aria-selected": it.id === current,
    onClick: () => {
      setInternal(it.id);
      onChange && onChange(it.id);
    }
  }, indexed && /*#__PURE__*/React.createElement("span", {
    className: "mt-tab-index"
  }, String(i + 1).padStart(2, '0')), it.label))), activeItem && activeItem.content !== undefined && /*#__PURE__*/React.createElement("div", {
    className: "mt-tab-panel",
    role: "tabpanel"
  }, activeItem.content));
}
Object.assign(__ds_scope, { Tabs });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Tabs.jsx", error: String((e && e.message) || e) }); }

// components/display/Tag.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-tag{display:inline-flex;align-items:center;height:22px;padding:0 10px;border:1px solid var(--border);border-radius:var(--radius-pill);font:400 10.5px var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--text-secondary);white-space:nowrap;background:transparent;text-decoration:none;transition:background var(--duration-fast) var(--ease-mech),color var(--duration-fast) var(--ease-mech),border-color var(--duration-fast) var(--ease-mech)}
.mt-tag[data-filled="true"]{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-tag[data-interactive="true"]{cursor:pointer}
.mt-tag[data-interactive="true"]:hover{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-tag[data-filled="true"][data-interactive="true"]:hover{background:transparent;color:var(--text-primary);border-color:var(--border-strong)}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-tag-css')) {
  const s = document.createElement('style');
  s.id = 'mt-tag-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Tag({
  filled = false,
  href,
  onClick,
  children,
  style,
  ...rest
}) {
  const interactive = !!(href || onClick);
  const Tag_ = href ? 'a' : onClick ? 'button' : 'span';
  return /*#__PURE__*/React.createElement(Tag_, _extends({
    className: "mt-tag",
    "data-filled": filled || undefined,
    "data-interactive": interactive || undefined,
    href: href,
    onClick: onClick,
    style: style
  }, rest), children);
}
Object.assign(__ds_scope, { Tag });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/display/Tag.jsx", error: String((e && e.message) || e) }); }

// components/forms/Checkbox.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-check{display:inline-flex;align-items:center;gap:10px;cursor:pointer;user-select:none}
.mt-check input{position:absolute;opacity:0;width:0;height:0}
.mt-check-box{width:16px;height:16px;border:1px solid var(--border-strong);display:inline-grid;place-items:center;flex:none;transition:background var(--duration-fast) var(--ease-mech),border-color var(--duration-fast) var(--ease-mech)}
.mt-check-box::after{content:'✕';font:700 10px/1 var(--font-mono);color:var(--text-inverse);opacity:0;transform:scale(.5);transition:opacity var(--duration-instant) linear,transform var(--duration-fast) var(--ease-mech)}
.mt-check input:checked + .mt-check-box{background:var(--bg-inverse);border-color:var(--bg-inverse)}
.mt-check input:checked + .mt-check-box::after{opacity:1;transform:scale(1)}
.mt-check input:focus-visible + .mt-check-box{outline:2px solid var(--focus-ring);outline-offset:2px}
.mt-check:hover .mt-check-box{border-color:var(--text-primary)}
.mt-check-label{font-family:var(--font-sans);font-size:13.5px;color:var(--text-primary)}
.mt-check[data-disabled="true"]{opacity:.35;pointer-events:none}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-check-css')) {
  const s = document.createElement('style');
  s.id = 'mt-check-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Checkbox({
  label,
  disabled = false,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", {
    className: "mt-check",
    "data-disabled": disabled || undefined,
    style: style
  }, /*#__PURE__*/React.createElement("input", _extends({
    type: "checkbox",
    disabled: disabled
  }, rest)), /*#__PURE__*/React.createElement("span", {
    className: "mt-check-box",
    "aria-hidden": "true"
  }), label && /*#__PURE__*/React.createElement("span", {
    className: "mt-check-label"
  }, label));
}
Object.assign(__ds_scope, { Checkbox });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Checkbox.jsx", error: String((e && e.message) || e) }); }

// components/forms/Input.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-field{display:flex;flex-direction:column;gap:6px}
.mt-field-label{font:500 10.5px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-secondary)}
.mt-input{font-family:var(--font-mono);font-size:13px;color:var(--text-primary);background:transparent;border:1px solid var(--border-strong);border-radius:var(--radius-sm);padding:10px 12px;width:100%;transition:border-color var(--duration-fast) var(--ease-out)}
.mt-input::placeholder{color:var(--text-tertiary)}
.mt-input:focus{outline:none;border-color:var(--text-primary)}
.mt-input[data-error="true"]{border-color:var(--negative)}
.mt-input:disabled{opacity:.35;cursor:not-allowed}
.mt-field-hint{font:400 10.5px var(--font-mono);letter-spacing:.06em;color:var(--text-tertiary)}
.mt-field-hint[data-error="true"]{color:var(--negative)}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-input-css')) {
  const s = document.createElement('style');
  s.id = 'mt-input-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Input({
  label,
  hint,
  error,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", {
    className: "mt-field",
    style: style
  }, label && /*#__PURE__*/React.createElement("span", {
    className: "mt-field-label"
  }, label), /*#__PURE__*/React.createElement("input", _extends({
    className: "mt-input",
    "data-error": !!error || undefined
  }, rest)), (error || hint) && /*#__PURE__*/React.createElement("span", {
    className: "mt-field-hint",
    "data-error": !!error || undefined
  }, error || hint));
}
Object.assign(__ds_scope, { Input });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Input.jsx", error: String((e && e.message) || e) }); }

// components/forms/Select.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-select-wrap{position:relative;display:block;width:100%}
.mt-select{appearance:none;-webkit-appearance:none;font-family:var(--font-mono);font-size:13px;color:var(--text-primary);background:transparent;border:1px solid var(--border-strong);border-radius:var(--radius-sm);padding:10px 36px 10px 12px;width:100%;cursor:pointer;transition:border-color var(--duration-fast) var(--ease-out)}
.mt-select:focus{outline:none;border-color:var(--text-primary)}
.mt-select:disabled{opacity:.35;cursor:not-allowed}
.mt-select option{background:var(--gray-900);color:var(--text-primary)}
[data-theme="light"] .mt-select option{background:var(--white);color:var(--black)}
.mt-select-chev{position:absolute;right:12px;top:50%;transform:translateY(-50%);pointer-events:none;font-family:var(--font-mono);font-size:10px;color:var(--text-secondary)}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-select-css')) {
  const s = document.createElement('style');
  s.id = 'mt-select-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Select({
  label,
  hint,
  options = [],
  placeholder,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", {
    className: "mt-field",
    style: style
  }, label && /*#__PURE__*/React.createElement("span", {
    className: "mt-field-label"
  }, label), /*#__PURE__*/React.createElement("span", {
    className: "mt-select-wrap"
  }, /*#__PURE__*/React.createElement("select", _extends({
    className: "mt-select",
    defaultValue: rest.value === undefined && placeholder ? '' : undefined
  }, rest), placeholder && /*#__PURE__*/React.createElement("option", {
    value: "",
    disabled: true
  }, placeholder), options.map(o => {
    const v = typeof o === 'string' ? {
      value: o,
      label: o
    } : o;
    return /*#__PURE__*/React.createElement("option", {
      key: v.value,
      value: v.value
    }, v.label);
  })), /*#__PURE__*/React.createElement("span", {
    className: "mt-select-chev",
    "aria-hidden": "true"
  }, "\u25BC")), hint && /*#__PURE__*/React.createElement("span", {
    className: "mt-field-hint"
  }, hint));
}
Object.assign(__ds_scope, { Select });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Select.jsx", error: String((e && e.message) || e) }); }

// components/forms/Switch.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-switch{display:inline-flex;align-items:center;gap:10px;cursor:pointer;user-select:none}
.mt-switch input{position:absolute;opacity:0;width:0;height:0}
.mt-switch-track{width:40px;height:22px;border:1px solid var(--border-strong);border-radius:var(--radius-pill);position:relative;flex:none;transition:background var(--duration-fast) var(--ease-mech),border-color var(--duration-fast) var(--ease-mech)}
.mt-switch-knob{position:absolute;top:3px;left:3px;width:14px;height:14px;border-radius:50%;background:var(--text-secondary);transition:left var(--duration-fast) var(--ease-mech),background var(--duration-fast) var(--ease-mech)}
.mt-switch input:checked + .mt-switch-track{background:var(--bg-inverse);border-color:var(--bg-inverse)}
.mt-switch input:checked + .mt-switch-track .mt-switch-knob{left:21px;background:var(--text-inverse)}
.mt-switch input:focus-visible + .mt-switch-track{outline:2px solid var(--focus-ring);outline-offset:2px}
.mt-switch:hover .mt-switch-track{border-color:var(--text-primary)}
.mt-switch-label{font:500 10.5px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-secondary)}
.mt-switch[data-disabled="true"]{opacity:.35;pointer-events:none}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-switch-css')) {
  const s = document.createElement('style');
  s.id = 'mt-switch-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Switch({
  label,
  disabled = false,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", {
    className: "mt-switch",
    "data-disabled": disabled || undefined,
    style: style
  }, /*#__PURE__*/React.createElement("input", _extends({
    type: "checkbox",
    role: "switch",
    disabled: disabled
  }, rest)), /*#__PURE__*/React.createElement("span", {
    className: "mt-switch-track",
    "aria-hidden": "true"
  }, /*#__PURE__*/React.createElement("span", {
    className: "mt-switch-knob"
  })), label && /*#__PURE__*/React.createElement("span", {
    className: "mt-switch-label"
  }, label));
}
Object.assign(__ds_scope, { Switch });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Switch.jsx", error: String((e && e.message) || e) }); }

// components/forms/Textarea.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
const css = `
.mt-textarea{font-family:var(--font-mono);font-size:13px;line-height:1.6;color:var(--text-primary);background:transparent;border:1px solid var(--border-strong);border-radius:var(--radius-sm);padding:10px 12px;width:100%;min-height:96px;resize:vertical;transition:border-color var(--duration-fast) var(--ease-out)}
.mt-textarea::placeholder{color:var(--text-tertiary)}
.mt-textarea:focus{outline:none;border-color:var(--text-primary)}
.mt-textarea[data-error="true"]{border-color:var(--negative)}
.mt-textarea:disabled{opacity:.35;cursor:not-allowed}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-textarea-css')) {
  const s = document.createElement('style');
  s.id = 'mt-textarea-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Textarea({
  label,
  hint,
  error,
  style,
  ...rest
}) {
  return /*#__PURE__*/React.createElement("label", {
    className: "mt-field",
    style: style
  }, label && /*#__PURE__*/React.createElement("span", {
    className: "mt-field-label"
  }, label), /*#__PURE__*/React.createElement("textarea", _extends({
    className: "mt-textarea",
    "data-error": !!error || undefined
  }, rest)), (error || hint) && /*#__PURE__*/React.createElement("span", {
    className: "mt-field-hint",
    "data-error": !!error || undefined
  }, error || hint));
}
Object.assign(__ds_scope, { Textarea });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/forms/Textarea.jsx", error: String((e && e.message) || e) }); }

// components/motifs/Barcode.jsx
try { (() => {
function Barcode({
  bars = 44,
  width = 220,
  height = 40,
  seed = 7,
  label,
  color = 'currentColor',
  style
}) {
  let s = seed >>> 0 || 1;
  const rnd = () => {
    s ^= s << 13;
    s ^= s >>> 17;
    s ^= s << 5;
    return (s >>> 0) % 1000 / 1000;
  };
  const rects = [];
  const unit = 100 / (bars * 2.2);
  let x = 0;
  for (let i = 0; i < bars && x < 100; i++) {
    const w = unit * (0.6 + rnd() * 2.4);
    rects.push(/*#__PURE__*/React.createElement("rect", {
      key: i,
      x: x,
      y: "0",
      width: Math.min(w, 100 - x),
      height: "100"
    }));
    x += w + unit * (0.5 + rnd() * 1.6);
  }
  return /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'inline-flex',
      flexDirection: 'column',
      gap: 6,
      ...style
    }
  }, /*#__PURE__*/React.createElement("svg", {
    viewBox: "0 0 100 100",
    preserveAspectRatio: "none",
    width: width,
    height: height,
    "aria-hidden": "true",
    style: {
      display: 'block'
    },
    fill: color
  }, rects), label && /*#__PURE__*/React.createElement("span", {
    style: {
      font: '400 9.5px var(--font-mono)',
      letterSpacing: '0.2em',
      textTransform: 'uppercase',
      color: 'var(--text-tertiary)',
      textAlign: 'center'
    }
  }, label));
}
Object.assign(__ds_scope, { Barcode });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/motifs/Barcode.jsx", error: String((e && e.message) || e) }); }

// components/motifs/DitherImage.jsx
try { (() => {
const css = `
.mt-dither{margin:0;position:relative;overflow:hidden}
.mt-dither img{display:block;width:100%;height:100%;object-fit:cover;filter:var(--img-filter)}
.mt-dither-overlay{position:absolute;inset:0;pointer-events:none}
.mt-dither-overlay[data-t="scanlines"]{background:repeating-linear-gradient(0deg,rgba(0,0,0,.45) 0 1px,transparent 1px 3px)}
.mt-dither-overlay[data-t="dots"]{background-image:radial-gradient(rgba(0,0,0,.55) 1px,transparent 1.3px);background-size:4px 4px}
.mt-dither-cap{display:flex;justify-content:space-between;gap:16px;font:400 10px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-tertiary);margin-top:8px}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-dither-css')) {
  const s = document.createElement('style');
  s.id = 'mt-dither-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function DitherImage({
  src,
  alt = '',
  ratio = '4 / 3',
  treatment = 'plain',
  caption,
  index,
  style
}) {
  return /*#__PURE__*/React.createElement("figure", {
    style: {
      margin: 0,
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-dither",
    style: {
      aspectRatio: ratio
    }
  }, /*#__PURE__*/React.createElement("img", {
    src: src,
    alt: alt
  }), treatment !== 'plain' && /*#__PURE__*/React.createElement("div", {
    className: "mt-dither-overlay",
    "data-t": treatment
  })), (caption || index) && /*#__PURE__*/React.createElement("figcaption", {
    className: "mt-dither-cap"
  }, /*#__PURE__*/React.createElement("span", null, caption), index && /*#__PURE__*/React.createElement("span", null, "[", index, "]")));
}
Object.assign(__ds_scope, { DitherImage });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/motifs/DitherImage.jsx", error: String((e && e.message) || e) }); }

// components/motifs/Globe.jsx
try { (() => {
function Globe({
  size = 200,
  meridians = 6,
  parallels = 5,
  tilt = 0.22,
  dotted = false,
  color = 'currentColor',
  strokeWidth = 1,
  spin = false,
  style
}) {
  const R = 100,
    els = [];
  for (let i = 1; i < meridians; i++) {
    const rx = R * Math.abs(Math.cos(i / meridians * Math.PI));
    if (rx < 1.5) els.push(/*#__PURE__*/React.createElement("line", {
      key: 'm' + i,
      x1: "0",
      y1: -R,
      x2: "0",
      y2: R
    }));else els.push(/*#__PURE__*/React.createElement("ellipse", {
      key: 'm' + i,
      cx: "0",
      cy: "0",
      rx: rx,
      ry: R
    }));
  }
  for (let j = 1; j <= parallels; j++) {
    const phi = -Math.PI / 2 + j * Math.PI / (parallels + 1);
    const rx = R * Math.cos(phi),
      cy = R * Math.sin(phi);
    els.push(/*#__PURE__*/React.createElement("ellipse", {
      key: 'p' + j,
      cx: "0",
      cy: cy,
      rx: rx,
      ry: Math.max(rx * tilt, 0.5)
    }));
  }
  if (spin && typeof document !== 'undefined' && !document.getElementById('mt-globe-css')) {
    const s = document.createElement('style');
    s.id = 'mt-globe-css';
    s.textContent = '@keyframes mt-globe-spin{to{transform:rotate(360deg)}}';
    document.head.appendChild(s);
  }
  return /*#__PURE__*/React.createElement("svg", {
    viewBox: "-106 -106 212 212",
    width: size,
    height: size,
    "aria-hidden": "true",
    style: {
      display: 'block',
      animation: spin ? 'mt-globe-spin 40s linear infinite' : undefined,
      ...style
    },
    fill: "none",
    stroke: color,
    strokeWidth: strokeWidth,
    strokeDasharray: dotted ? `${strokeWidth * 0.2} ${strokeWidth * 3.2}` : undefined,
    strokeLinecap: dotted ? 'round' : undefined
  }, /*#__PURE__*/React.createElement("circle", {
    cx: "0",
    cy: "0",
    r: R,
    strokeDasharray: "none"
  }), els);
}
Object.assign(__ds_scope, { Globe });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/motifs/Globe.jsx", error: String((e && e.message) || e) }); }

// components/motifs/HazardTape.jsx
try { (() => {
function HazardTape({
  height = 14,
  stripe = 10,
  angle = -45,
  color = 'var(--text-primary)',
  framed = true,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    "aria-hidden": "true",
    style: {
      height,
      width: '100%',
      borderTop: framed ? '1px solid var(--border-strong)' : 'none',
      borderBottom: framed ? '1px solid var(--border-strong)' : 'none',
      background: `repeating-linear-gradient(${angle}deg, ${color} 0 ${stripe}px, transparent ${stripe}px ${stripe * 2}px)`,
      ...style
    }
  });
}
Object.assign(__ds_scope, { HazardTape });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/motifs/HazardTape.jsx", error: String((e && e.message) || e) }); }

// components/motifs/Starburst.jsx
try { (() => {
function Starburst({
  shape = 'sparkle',
  size = 48,
  points,
  color = 'currentColor',
  strokeWidth = 1.5,
  style
}) {
  const R = 50;
  let node = null;
  if (shape === 'sparkle') {
    const inner = R * 0.16;
    let d = `M0 ${-R}`;
    for (let k = 0; k < 4; k++) {
      const a = (k * 90 + 45) * Math.PI / 180,
        na = (k + 1) % 4 * 90 * Math.PI / 180;
      d += `Q${(inner * Math.sin(a)).toFixed(1)} ${(-inner * Math.cos(a)).toFixed(1)} ${(R * Math.sin(na)).toFixed(1)} ${(-R * Math.cos(na)).toFixed(1)}`;
    }
    node = /*#__PURE__*/React.createElement("path", {
      d: d + 'Z',
      fill: color
    });
  } else if (shape === 'burst') {
    const n = points || 24,
      lines = [];
    for (let i = 0; i < n; i++) {
      const a = i / n * 2 * Math.PI,
        r0 = R * 0.22;
      lines.push(/*#__PURE__*/React.createElement("line", {
        key: i,
        x1: r0 * Math.cos(a),
        y1: r0 * Math.sin(a),
        x2: R * Math.cos(a),
        y2: R * Math.sin(a)
      }));
    }
    node = /*#__PURE__*/React.createElement("g", {
      stroke: color,
      strokeWidth: strokeWidth
    }, lines);
  } else if (shape === 'sun') {
    const n = points || 16;
    let d = '';
    for (let i = 0; i < 2 * n; i++) {
      const a = i / (2 * n) * 2 * Math.PI - Math.PI / 2,
        r = i % 2 ? R * 0.55 : R;
      d += (i ? 'L' : 'M') + (r * Math.cos(a)).toFixed(1) + ' ' + (r * Math.sin(a)).toFixed(1);
    }
    node = /*#__PURE__*/React.createElement("path", {
      d: d + 'Z',
      fill: color
    });
  } else {
    const n = points || 6,
      petals = [];
    for (let i = 0; i < n; i++) petals.push(/*#__PURE__*/React.createElement("ellipse", {
      key: i,
      cx: "0",
      cy: -R * 0.55,
      rx: R * 0.3,
      ry: R * 0.48,
      fill: color,
      transform: `rotate(${i / n * 360})`
    }));
    node = /*#__PURE__*/React.createElement("g", null, petals);
  }
  return /*#__PURE__*/React.createElement("svg", {
    viewBox: "-54 -54 108 108",
    width: size,
    height: size,
    "aria-hidden": "true",
    style: {
      display: 'block',
      ...style
    }
  }, node);
}
Object.assign(__ds_scope, { Starburst });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/motifs/Starburst.jsx", error: String((e && e.message) || e) }); }

// components/motifs/WarpGrid.jsx
try { (() => {
function WarpGrid({
  width = 320,
  height = 220,
  cols = 14,
  rows = 10,
  amp = 9,
  freq = 1.7,
  seed = 2,
  color = 'currentColor',
  strokeWidth = 1,
  style
}) {
  const N = 36,
    paths = [];
  const wave = (t, phase) => Math.sin(t * Math.PI * freq + phase + seed);
  for (let r = 0; r <= rows; r++) {
    const y0 = r / rows * height,
      ph = r * 0.7;
    let d = '';
    for (let k = 0; k <= N; k++) {
      const x = k / N * width;
      const y = y0 + amp * wave(k / N, ph) * Math.sin(r / rows * Math.PI * 0.9 + 0.3);
      d += (k ? 'L' : 'M') + x.toFixed(1) + ' ' + y.toFixed(1);
    }
    paths.push(/*#__PURE__*/React.createElement("path", {
      key: 'h' + r,
      d: d
    }));
  }
  for (let c = 0; c <= cols; c++) {
    const x0 = c / cols * width,
      ph = c * 0.9 + 2;
    let d = '';
    for (let k = 0; k <= N; k++) {
      const y = k / N * height;
      const x = x0 + amp * wave(k / N, ph) * Math.sin(c / cols * Math.PI * 0.9 + 0.3);
      d += (k ? 'L' : 'M') + x.toFixed(1) + ' ' + y.toFixed(1);
    }
    paths.push(/*#__PURE__*/React.createElement("path", {
      key: 'v' + c,
      d: d
    }));
  }
  const pad = amp + strokeWidth;
  return /*#__PURE__*/React.createElement("svg", {
    viewBox: `${-pad} ${-pad} ${width + 2 * pad} ${height + 2 * pad}`,
    width: width,
    height: height,
    "aria-hidden": "true",
    style: {
      display: 'block',
      ...style
    },
    fill: "none",
    stroke: color,
    strokeWidth: strokeWidth
  }, paths);
}
Object.assign(__ds_scope, { WarpGrid });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/motifs/WarpGrid.jsx", error: String((e && e.message) || e) }); }

// components/site/Footer.jsx
try { (() => {
const css = `
.mt-footer{border-top:1px solid var(--border-strong);background:var(--bg)}
.mt-footer-name{font-family:var(--font-display);text-transform:uppercase;line-height:.92;letter-spacing:-0.01em;color:transparent;-webkit-text-stroke:1.5px var(--text-primary);font-size:clamp(48px,9.5vw,140px);margin:0;padding:40px 24px 8px;white-space:nowrap;overflow:hidden}
.mt-footer-name[data-solid="true"]{color:var(--text-primary);-webkit-text-stroke:0}
.mt-footer-grid{display:flex;flex-wrap:wrap;gap:40px;padding:24px;border-top:1px solid var(--border)}
.mt-footer-col{display:flex;flex-direction:column;gap:10px;min-width:140px}
.mt-footer-col h4{font:500 10px var(--font-mono);letter-spacing:var(--tracking-wide);text-transform:uppercase;color:var(--text-tertiary);margin:0 0 4px}
.mt-footer-col a{font:400 11px var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--text-secondary);text-decoration:none}
.mt-footer-col a:hover{color:var(--link-hover)}
.mt-footer-bottom{display:flex;align-items:center;gap:24px;padding:16px 24px;border-top:1px solid var(--border);font:400 10px var(--font-mono);letter-spacing:.1em;text-transform:uppercase;color:var(--text-tertiary);flex-wrap:wrap}
.mt-footer-bottom .spacer{flex:1}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-footer-css')) {
  const s = document.createElement('style');
  s.id = 'mt-footer-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Footer({
  name = 'Mickael Teixeira',
  solid = false,
  columns = [],
  legal = '©2026 Mickael Teixeira',
  coords = "48°51'24\"N 2°21'08\"E",
  extra,
  style
}) {
  return /*#__PURE__*/React.createElement("footer", {
    className: "mt-footer",
    style: style
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-footer-name",
    "data-solid": solid || undefined
  }, name), columns.length > 0 && /*#__PURE__*/React.createElement("div", {
    className: "mt-footer-grid"
  }, columns.map(c => /*#__PURE__*/React.createElement("div", {
    key: c.title,
    className: "mt-footer-col"
  }, /*#__PURE__*/React.createElement("h4", null, c.title), c.links.map(l => /*#__PURE__*/React.createElement("a", {
    key: l.label,
    href: l.href || '#'
  }, l.label, " \u2197"))))), /*#__PURE__*/React.createElement("div", {
    className: "mt-footer-bottom"
  }, /*#__PURE__*/React.createElement("span", null, legal), /*#__PURE__*/React.createElement("span", null, coords), /*#__PURE__*/React.createElement("span", {
    className: "spacer"
  }), extra));
}
Object.assign(__ds_scope, { Footer });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/site/Footer.jsx", error: String((e && e.message) || e) }); }

// components/site/ProjectCard.jsx
try { (() => {
const css = `
.mt-projcard{display:block;border:1px solid var(--border);background:var(--surface-card);text-decoration:none;cursor:pointer;transition:border-color var(--duration-fast) var(--ease-out);text-align:left;padding:0;width:100%}
.mt-projcard:hover{border-color:var(--border-strong)}
.mt-projcard-img{aspect-ratio:4/3;overflow:hidden;border-bottom:1px solid var(--border);position:relative;background:var(--gray-950)}
.mt-projcard-img img{width:100%;height:100%;object-fit:cover;display:block;filter:var(--img-filter);transition:transform var(--duration-base) var(--ease-mech)}
.mt-projcard:hover .mt-projcard-img img{transform:scale(1.03)}
.mt-projcard-body{padding:14px 16px}
.mt-projcard-top{display:flex;align-items:baseline;gap:12px}
.mt-projcard-idx{font:400 10px var(--font-mono);letter-spacing:.1em;color:var(--text-tertiary)}
.mt-projcard-title{font-family:var(--font-display);font-size:15px;letter-spacing:.01em;text-transform:uppercase;color:var(--text-primary);margin:0;flex:1}
.mt-projcard-arrow{font-size:14px;color:var(--text-secondary);transition:transform var(--duration-fast) var(--ease-mech),color var(--duration-fast)}
.mt-projcard:hover .mt-projcard-arrow{transform:translate(2px,-2px);color:var(--link-hover)}
.mt-projcard-tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px;font:400 9.5px var(--font-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--text-tertiary)}
.mt-projcard-tags span{border:1px solid var(--border);border-radius:var(--radius-pill);padding:2px 8px}
.mt-projcard-year{font:400 10px var(--font-mono);color:var(--text-tertiary)}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-projcard-css')) {
  const s = document.createElement('style');
  s.id = 'mt-projcard-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function ProjectCard({
  index = '01',
  title,
  year = '2026',
  tags = [],
  image,
  imageNode,
  href,
  onClick,
  style
}) {
  const Tag_ = href ? 'a' : 'button';
  return /*#__PURE__*/React.createElement(Tag_, {
    className: "mt-projcard",
    href: href,
    onClick: onClick,
    style: style
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-projcard-img"
  }, imageNode || image && /*#__PURE__*/React.createElement("img", {
    src: image,
    alt: title
  })), /*#__PURE__*/React.createElement("div", {
    className: "mt-projcard-body"
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-projcard-top"
  }, /*#__PURE__*/React.createElement("span", {
    className: "mt-projcard-idx"
  }, "[", index, "]"), /*#__PURE__*/React.createElement("h3", {
    className: "mt-projcard-title"
  }, title), /*#__PURE__*/React.createElement("span", {
    className: "mt-projcard-year"
  }, "(", year, ")"), /*#__PURE__*/React.createElement("span", {
    className: "mt-projcard-arrow",
    "aria-hidden": "true"
  }, "\u2197")), tags.length > 0 && /*#__PURE__*/React.createElement("div", {
    className: "mt-projcard-tags"
  }, tags.map(t => /*#__PURE__*/React.createElement("span", {
    key: t
  }, t)))));
}
Object.assign(__ds_scope, { ProjectCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/site/ProjectCard.jsx", error: String((e && e.message) || e) }); }

// components/site/SiteNav.jsx
try { (() => {
const css = `
.mt-nav{height:var(--nav-height);display:flex;align-items:center;gap:40px;padding:0 24px;border-bottom:1px solid var(--border);background:var(--bg);position:relative;z-index:var(--z-nav)}
.mt-nav-name{font:700 12px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-primary);text-decoration:none;white-space:nowrap;cursor:pointer;background:none;border:0;padding:0}
.mt-nav-links{display:flex;gap:28px;margin-left:auto}
.mt-nav-link{font:500 10.5px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-secondary);background:none;border:0;padding:0;cursor:pointer;transition:color var(--duration-fast) var(--ease-out)}
.mt-nav-link:hover{color:var(--link-hover)}
.mt-nav-link[data-active="true"]{color:var(--text-primary);text-decoration:underline;text-underline-offset:5px}
.mt-nav-link-idx{color:var(--text-tertiary);margin-right:5px}
.mt-nav-right{display:flex;align-items:center;gap:16px}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-nav-css')) {
  const s = document.createElement('style');
  s.id = 'mt-nav-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function SiteNav({
  name = 'Mickael Teixeira',
  links = [],
  active,
  onNavigate,
  right,
  style
}) {
  return /*#__PURE__*/React.createElement("header", {
    className: "mt-nav",
    style: style
  }, /*#__PURE__*/React.createElement("button", {
    className: "mt-nav-name",
    onClick: () => onNavigate && onNavigate('home')
  }, name, /*#__PURE__*/React.createElement("sup", null, "\xAE")), /*#__PURE__*/React.createElement("nav", {
    className: "mt-nav-links"
  }, links.map((l, i) => {
    const item = typeof l === 'string' ? {
      id: l,
      label: l
    } : l;
    return /*#__PURE__*/React.createElement("button", {
      key: item.id,
      className: "mt-nav-link",
      "data-active": item.id === active || undefined,
      onClick: () => onNavigate && onNavigate(item.id)
    }, /*#__PURE__*/React.createElement("span", {
      className: "mt-nav-link-idx"
    }, String(i + 1).padStart(2, '0')), item.label);
  })), right && /*#__PURE__*/React.createElement("div", {
    className: "mt-nav-right"
  }, right));
}
Object.assign(__ds_scope, { SiteNav });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/site/SiteNav.jsx", error: String((e && e.message) || e) }); }

// components/typography/Marquee.jsx
try { (() => {
const css = `
.mt-marquee{overflow:hidden;white-space:nowrap;border-top:1px solid var(--border);border-bottom:1px solid var(--border);user-select:none}
.mt-marquee[data-filled="true"]{background:var(--bg-inverse);color:var(--text-inverse);border-color:var(--bg-inverse)}
.mt-marquee-inner{display:inline-flex;animation:mt-marquee var(--mt-marquee-dur,22s) linear infinite}
.mt-marquee[data-reverse="true"] .mt-marquee-inner{animation-direction:reverse}
.mt-marquee-group{display:inline-flex;align-items:center;gap:40px;padding-right:40px}
.mt-marquee-sep{opacity:.5}
@keyframes mt-marquee{to{transform:translateX(-50%)}}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-marquee-css')) {
  const s = document.createElement('style');
  s.id = 'mt-marquee-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function Marquee({
  text = '',
  separator = '✦',
  font = 'display',
  size = 40,
  duration = 22,
  reverse = false,
  filled = false,
  repeat = 6,
  style
}) {
  const items = [];
  for (let i = 0; i < repeat; i++) items.push(/*#__PURE__*/React.createElement(React.Fragment, {
    key: i
  }, /*#__PURE__*/React.createElement("span", null, text), /*#__PURE__*/React.createElement("span", {
    className: "mt-marquee-sep",
    "aria-hidden": "true"
  }, separator)));
  const fontCss = font === 'display' ? {
    fontFamily: 'var(--font-display)',
    letterSpacing: 'var(--tracking-display)'
  } : {
    fontFamily: 'var(--font-mono)',
    fontWeight: 500,
    letterSpacing: 'var(--tracking-caps)'
  };
  return /*#__PURE__*/React.createElement("div", {
    className: "mt-marquee",
    "data-filled": filled || undefined,
    "data-reverse": reverse || undefined,
    role: "presentation",
    style: {
      '--mt-marquee-dur': duration + 's',
      ...style
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-marquee-inner",
    style: {
      ...fontCss,
      fontSize: size,
      textTransform: 'uppercase',
      lineHeight: 1.6
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: "mt-marquee-group"
  }, items), /*#__PURE__*/React.createElement("div", {
    className: "mt-marquee-group",
    "aria-hidden": "true"
  }, items)));
}
Object.assign(__ds_scope, { Marquee });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/typography/Marquee.jsx", error: String((e && e.message) || e) }); }

// components/typography/MetaTable.jsx
try { (() => {
const css = `
.mt-meta{font-family:var(--font-mono);text-transform:uppercase}
.mt-meta-row{display:grid;grid-template-columns:var(--mt-meta-col,132px) 1fr;gap:16px;padding:9px 0;border-bottom:1px solid var(--border)}
.mt-meta-row:first-child{border-top:1px solid var(--border)}
.mt-meta[data-divided="false"] .mt-meta-row{border:none;padding:5px 0}
.mt-meta-k{font-size:10px;letter-spacing:var(--tracking-caps);color:var(--text-tertiary)}
.mt-meta-v{font-size:11px;letter-spacing:.08em;color:var(--text-primary)}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-meta-css')) {
  const s = document.createElement('style');
  s.id = 'mt-meta-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function MetaTable({
  rows = [],
  divided = true,
  labelWidth = 132,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "mt-meta",
    "data-divided": divided,
    style: {
      '--mt-meta-col': labelWidth + 'px',
      ...style
    }
  }, rows.map((r, i) => /*#__PURE__*/React.createElement("div", {
    key: i,
    className: "mt-meta-row"
  }, /*#__PURE__*/React.createElement("span", {
    className: "mt-meta-k"
  }, r.k), /*#__PURE__*/React.createElement("span", {
    className: "mt-meta-v"
  }, r.v))));
}
Object.assign(__ds_scope, { MetaTable });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/typography/MetaTable.jsx", error: String((e && e.message) || e) }); }

// components/typography/SectionHeader.jsx
try { (() => {
const css = `
.mt-secthead{display:flex;align-items:baseline;gap:16px;border-bottom:1px solid var(--border);padding-bottom:14px}
.mt-secthead-idx{font:400 11px var(--font-mono);letter-spacing:.1em;color:var(--text-tertiary);flex:none}
.mt-secthead-title{font-family:var(--font-display);font-size:26px;line-height:1;letter-spacing:var(--tracking-display);text-transform:uppercase;color:var(--text-primary);margin:0}
.mt-secthead-meta{font:400 10.5px var(--font-mono);letter-spacing:var(--tracking-caps);text-transform:uppercase;color:var(--text-secondary);margin-left:auto;flex:none}`;
if (typeof document !== 'undefined' && !document.getElementById('mt-secthead-css')) {
  const s = document.createElement('style');
  s.id = 'mt-secthead-css';
  s.textContent = css;
  document.head.appendChild(s);
}
function SectionHeader({
  index = '01',
  title,
  meta,
  rule = true,
  style
}) {
  return /*#__PURE__*/React.createElement("div", {
    className: "mt-secthead",
    style: {
      borderBottom: rule ? undefined : 'none',
      ...style
    }
  }, /*#__PURE__*/React.createElement("span", {
    className: "mt-secthead-idx"
  }, "[", index, "]"), /*#__PURE__*/React.createElement("h2", {
    className: "mt-secthead-title"
  }, title), meta && /*#__PURE__*/React.createElement("span", {
    className: "mt-secthead-meta"
  }, meta));
}
Object.assign(__ds_scope, { SectionHeader });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/typography/SectionHeader.jsx", error: String((e && e.message) || e) }); }

// ui_kits/portfolio/AboutScreen.jsx
try { (() => {
const {
  useState
} = React;
function AboutScreen() {
  const NS = window.MickaelTeixeiraDesignSystem_e955b5;
  const {
    DitherImage,
    MetaTable,
    Tag,
    Card,
    Input,
    Textarea,
    Select,
    Checkbox,
    Button,
    SectionHeader
  } = NS;
  const [sent, setSent] = useState(false);
  const mono = {
    fontFamily: 'var(--font-mono)',
    textTransform: 'uppercase'
  };
  return /*#__PURE__*/React.createElement("div", {
    "data-screen-label": "\xC0 propos"
  }, /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '48px 24px 56px'
    }
  }, /*#__PURE__*/React.createElement(SectionHeader, {
    index: "03",
    title: "\xC0 propos",
    meta: "Paris, FR \u2014 Worldwide"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '300px 1fr',
      gap: 40,
      marginTop: 32,
      alignItems: 'start'
    }
  }, /*#__PURE__*/React.createElement(DitherImage, {
    src: "../../assets/img/dither-hands-touch.jpg",
    ratio: "3 / 4",
    treatment: "dots",
    caption: "Mickael Teixeira",
    index: "MT"
  }), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 26,
      lineHeight: 1.35,
      letterSpacing: '-0.01em',
      margin: '0 0 24px',
      fontWeight: 500
    }
  }, "Je con\xE7ois des identit\xE9s et des sites qui tiennent sur une id\xE9e ", /*#__PURE__*/React.createElement("em", {
    style: {
      fontFamily: 'var(--font-serif)',
      fontStyle: 'italic',
      fontSize: '1.1em',
      fontWeight: 400
    }
  }, "simple"), " \u2014 puis je les pousse jusqu'au pixel."), /*#__PURE__*/React.createElement("p", {
    style: {
      fontSize: 14,
      lineHeight: 1.7,
      color: 'var(--text-secondary)',
      margin: '0 0 28px',
      maxWidth: 560
    }
  }, "Designer graphique et d\xE9veloppeur cr\xE9atif. Apr\xE8s plusieurs ann\xE9es entre studios et projets ind\xE9pendants, je travaille aujourd'hui en direct avec des marques, des artistes et des \xE9quipes produit."), /*#__PURE__*/React.createElement(MetaTable, {
    rows: [{
      k: 'Base',
      v: 'Paris, France'
    }, {
      k: 'Expérience',
      v: '2019 — 2026'
    }, {
      k: 'Langues',
      v: 'FR / EN / PT'
    }, {
      k: 'Statut',
      v: 'Freelance — disponible'
    }]
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 8,
      flexWrap: 'wrap',
      marginTop: 24
    }
  }, ['Branding', 'Direction artistique', 'UI', 'Webgl', 'Motion', 'Print'].map(t => /*#__PURE__*/React.createElement(Tag, {
    key: t
  }, t)))))), /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '0 24px 64px'
    }
  }, /*#__PURE__*/React.createElement(SectionHeader, {
    index: "04",
    title: "Contact",
    meta: "R\xE9ponse sous 48h"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      maxWidth: 640,
      marginTop: 28
    }
  }, /*#__PURE__*/React.createElement(Card, {
    title: "Nouveau projet",
    meta: "[form]",
    corners: true
  }, sent ? /*#__PURE__*/React.createElement("div", {
    style: {
      ...mono,
      fontSize: 12,
      letterSpacing: '.12em',
      padding: '24px 0',
      textAlign: 'center'
    }
  }, "Message envoy\xE9 \u2014 merci. ", /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'var(--positive)'
    }
  }, "\u25CF")) : /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      flexDirection: 'column',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 16
    }
  }, /*#__PURE__*/React.createElement(Input, {
    label: "Nom",
    placeholder: "Votre nom"
  }), /*#__PURE__*/React.createElement(Input, {
    label: "Email",
    placeholder: "nom@exemple.fr"
  })), /*#__PURE__*/React.createElement(Select, {
    label: "Budget",
    placeholder: "Choisir\u2026",
    options: ['< 5k€', '5–15k€', '15k€ +', 'À définir']
  }), /*#__PURE__*/React.createElement(Textarea, {
    label: "Message",
    placeholder: "Parlez-moi de votre projet\u2026",
    rows: 4
  }), /*#__PURE__*/React.createElement(Checkbox, {
    label: "J'accepte d'\xEAtre recontact\xE9 par email",
    defaultChecked: true
  }), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    arrow: true,
    onClick: () => setSent(true)
  }, "Envoyer")))))));
}
Object.assign(__ds_scope, { AboutScreen });
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/portfolio/AboutScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/portfolio/HomeScreen.jsx
try { (() => {
function HomeScreen({
  projects = [],
  onOpenProject,
  onNavigate
}) {
  const NS = window.MickaelTeixeiraDesignSystem_e955b5;
  const {
    Globe,
    Marquee,
    SectionHeader,
    ProjectCard,
    Button,
    Starburst
  } = NS;
  const mono = {
    fontFamily: 'var(--font-mono)',
    textTransform: 'uppercase'
  };
  return /*#__PURE__*/React.createElement("div", {
    "data-screen-label": "Accueil"
  }, /*#__PURE__*/React.createElement("section", {
    style: {
      position: 'relative',
      padding: '48px 24px 64px',
      borderBottom: '1px solid var(--border)',
      overflow: 'hidden'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      ...mono,
      display: 'flex',
      justifyContent: 'space-between',
      fontSize: 10,
      letterSpacing: '.2em',
      color: 'var(--text-tertiary)',
      marginBottom: 48
    }
  }, /*#__PURE__*/React.createElement("span", null, "Portfolio \u2014 Vol.01"), /*#__PURE__*/React.createElement("span", null, "48\xB051'24\"N 2\xB021'08\"E \u2014 Paris, FR"), /*#__PURE__*/React.createElement("span", null, "(2026)")), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 40,
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      flex: 1,
      minWidth: 0
    }
  }, /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 'clamp(56px,8.5vw,118px)',
      lineHeight: 0.92,
      letterSpacing: '-0.01em',
      textTransform: 'uppercase',
      margin: 0
    }
  }, "Mickael", /*#__PURE__*/React.createElement("br", null), /*#__PURE__*/React.createElement("span", {
    style: {
      color: 'transparent',
      WebkitTextStroke: '1.5px var(--text-primary)'
    }
  }, "Teixeira")), /*#__PURE__*/React.createElement("p", {
    style: {
      ...mono,
      fontSize: 11.5,
      letterSpacing: '.12em',
      color: 'var(--text-secondary)',
      margin: '28px 0 32px',
      maxWidth: 460,
      lineHeight: 1.8
    }
  }, "Designer graphique & d\xE9veloppeur cr\xE9atif.", /*#__PURE__*/React.createElement("br", null), "Identit\xE9s, sites, installations \u2014 du concept au code."), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 12
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "primary",
    arrow: true,
    onClick: () => onOpenProject && onOpenProject(projects[0])
  }, "Voir les travaux"), /*#__PURE__*/React.createElement(Button, {
    variant: "outline",
    onClick: () => onNavigate && onNavigate('about')
  }, "Me contacter"))), /*#__PURE__*/React.createElement("div", {
    style: {
      position: 'relative',
      flex: 'none',
      color: 'var(--text-primary)'
    }
  }, /*#__PURE__*/React.createElement(Globe, {
    size: 330,
    spin: true
  }), /*#__PURE__*/React.createElement("span", {
    style: {
      position: 'absolute',
      top: -6,
      right: -10
    }
  }, /*#__PURE__*/React.createElement(Starburst, {
    shape: "sparkle",
    size: 26
  })), /*#__PURE__*/React.createElement("span", {
    style: {
      ...mono,
      position: 'absolute',
      bottom: -4,
      left: '50%',
      transform: 'translateX(-50%)',
      fontSize: 9,
      letterSpacing: '.2em',
      color: 'var(--text-tertiary)',
      whiteSpace: 'nowrap'
    }
  }, "Worldwide \u2014 remote OK")))), /*#__PURE__*/React.createElement(Marquee, {
    text: "Designer graphique \u2014 D\xE9veloppeur cr\xE9atif",
    size: 38,
    duration: 26
  }), /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '56px 24px'
    }
  }, /*#__PURE__*/React.createElement(SectionHeader, {
    index: "01",
    title: "Travaux s\xE9lectionn\xE9s",
    meta: "2024 \u2014 2026"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 20,
      marginTop: 28
    }
  }, projects.map(p => /*#__PURE__*/React.createElement(ProjectCard, {
    key: p.index,
    index: p.index,
    title: p.title,
    year: p.year,
    tags: p.tags,
    image: p.image,
    onClick: () => onOpenProject && onOpenProject(p)
  })))), /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '48px 24px 64px',
      borderTop: '1px solid var(--border)'
    }
  }, /*#__PURE__*/React.createElement(SectionHeader, {
    index: "02",
    title: "Services",
    meta: "Ce que je fais"
  }), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 1fr 1fr',
      gap: 20,
      marginTop: 28
    }
  }, [{
    n: '01',
    t: 'Identité visuelle',
    d: 'Logos typographiques, systèmes de marque, direction artistique print et digitale.'
  }, {
    n: '02',
    t: 'Sites & interfaces',
    d: 'Portfolios, vitrines et prototypes — design système, intégration soignée.'
  }, {
    n: '03',
    t: 'Créatif codé',
    d: 'Installations WebGL, affiches génératives, motifs paramétriques.'
  }].map(s => /*#__PURE__*/React.createElement("div", {
    key: s.n,
    style: {
      border: '1px solid var(--border)',
      padding: 20
    }
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      ...mono,
      fontSize: 10,
      letterSpacing: '.12em',
      color: 'var(--text-tertiary)',
      display: 'flex',
      justifyContent: 'space-between',
      marginBottom: 14
    }
  }, /*#__PURE__*/React.createElement("span", null, "[", s.n, "]"), /*#__PURE__*/React.createElement(Starburst, {
    shape: "sparkle",
    size: 14
  })), /*#__PURE__*/React.createElement("h3", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 17,
      textTransform: 'uppercase',
      margin: '0 0 10px'
    }
  }, s.t), /*#__PURE__*/React.createElement("p", {
    style: {
      margin: 0,
      fontSize: 13,
      lineHeight: 1.6,
      color: 'var(--text-secondary)'
    }
  }, s.d))))));
}
Object.assign(__ds_scope, { HomeScreen });
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/portfolio/HomeScreen.jsx", error: String((e && e.message) || e) }); }

// ui_kits/portfolio/ProjectScreen.jsx
try { (() => {
function ProjectScreen({
  project,
  onBack,
  onNext
}) {
  const NS = window.MickaelTeixeiraDesignSystem_e955b5;
  const {
    MetaTable,
    DitherImage,
    Button,
    Tag,
    HazardTape
  } = NS;
  const p = project || {};
  const mono = {
    fontFamily: 'var(--font-mono)',
    textTransform: 'uppercase'
  };
  return /*#__PURE__*/React.createElement("div", {
    "data-screen-label": "Projet"
  }, /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '20px 24px',
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      borderBottom: '1px solid var(--border)'
    }
  }, /*#__PURE__*/React.createElement(Button, {
    variant: "ghost",
    size: "sm",
    onClick: onBack
  }, "\u2190 Index"), /*#__PURE__*/React.createElement("span", {
    style: {
      ...mono,
      fontSize: 10,
      letterSpacing: '.2em',
      color: 'var(--text-tertiary)',
      marginLeft: 'auto'
    }
  }, "Projet [", p.index, "] / 04")), /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '48px 24px 36px'
    }
  }, /*#__PURE__*/React.createElement("h1", {
    style: {
      fontFamily: 'var(--font-display)',
      fontSize: 'clamp(44px,6.5vw,88px)',
      lineHeight: 0.95,
      textTransform: 'uppercase',
      margin: '0 0 20px'
    }
  }, p.title), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'flex',
      gap: 8,
      marginBottom: 32
    }
  }, (p.tags || []).map(t => /*#__PURE__*/React.createElement(Tag, {
    key: t
  }, t))), /*#__PURE__*/React.createElement("div", {
    style: {
      display: 'grid',
      gridTemplateColumns: '1fr 360px',
      gap: 40,
      alignItems: 'start'
    }
  }, /*#__PURE__*/React.createElement(DitherImage, {
    src: p.image,
    ratio: "16 / 10",
    treatment: "scanlines",
    caption: p.title,
    index: p.index
  }), /*#__PURE__*/React.createElement(MetaTable, {
    rows: [{
      k: 'Client',
      v: p.client || '—'
    }, {
      k: 'Année',
      v: p.year
    }, {
      k: 'Catégorie',
      v: (p.tags || []).join(' / ')
    }, {
      k: 'Rôle',
      v: 'Design + Développement'
    }]
  }))), /*#__PURE__*/React.createElement("section", {
    style: {
      padding: '0 24px 56px',
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: 40
    }
  }, /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h2", {
    style: {
      ...mono,
      fontSize: 11,
      letterSpacing: '.2em',
      color: 'var(--text-tertiary)',
      margin: '0 0 12px'
    }
  }, "[A] \u2014 Contexte"), /*#__PURE__*/React.createElement("p", {
    style: {
      margin: 0,
      fontSize: 14,
      lineHeight: 1.7,
      color: 'var(--text-primary)'
    }
  }, p.brief)), /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h2", {
    style: {
      ...mono,
      fontSize: 11,
      letterSpacing: '.2em',
      color: 'var(--text-tertiary)',
      margin: '0 0 12px'
    }
  }, "[B] \u2014 Approche"), /*#__PURE__*/React.createElement("p", {
    style: {
      margin: 0,
      fontSize: 14,
      lineHeight: 1.7,
      color: 'var(--text-secondary)'
    }
  }, p.approach))), /*#__PURE__*/React.createElement(HazardTape, null), /*#__PURE__*/React.createElement("div", {
    style: {
      padding: '20px 24px 40px',
      display: 'flex',
      alignItems: 'center'
    }
  }, /*#__PURE__*/React.createElement("span", {
    style: {
      ...mono,
      fontSize: 10,
      letterSpacing: '.2em',
      color: 'var(--text-tertiary)'
    }
  }, "Projet suivant"), /*#__PURE__*/React.createElement("span", {
    style: {
      flex: 1
    }
  }), /*#__PURE__*/React.createElement(Button, {
    variant: "outline",
    arrow: true,
    onClick: onNext
  }, p.nextTitle || 'Suivant')));
}
Object.assign(__ds_scope, { ProjectScreen });
})(); } catch (e) { __ds_ns.__errors.push({ path: "ui_kits/portfolio/ProjectScreen.jsx", error: String((e && e.message) || e) }); }

__ds_ns.Button = __ds_scope.Button;

__ds_ns.IconButton = __ds_scope.IconButton;

__ds_ns.Badge = __ds_scope.Badge;

__ds_ns.Card = __ds_scope.Card;

__ds_ns.Tabs = __ds_scope.Tabs;

__ds_ns.Tag = __ds_scope.Tag;

__ds_ns.Checkbox = __ds_scope.Checkbox;

__ds_ns.Input = __ds_scope.Input;

__ds_ns.Select = __ds_scope.Select;

__ds_ns.Switch = __ds_scope.Switch;

__ds_ns.Textarea = __ds_scope.Textarea;

__ds_ns.Barcode = __ds_scope.Barcode;

__ds_ns.DitherImage = __ds_scope.DitherImage;

__ds_ns.Globe = __ds_scope.Globe;

__ds_ns.HazardTape = __ds_scope.HazardTape;

__ds_ns.Starburst = __ds_scope.Starburst;

__ds_ns.WarpGrid = __ds_scope.WarpGrid;

__ds_ns.Footer = __ds_scope.Footer;

__ds_ns.ProjectCard = __ds_scope.ProjectCard;

__ds_ns.SiteNav = __ds_scope.SiteNav;

__ds_ns.Marquee = __ds_scope.Marquee;

__ds_ns.MetaTable = __ds_scope.MetaTable;

__ds_ns.SectionHeader = __ds_scope.SectionHeader;

__ds_ns.AboutScreen = __ds_scope.AboutScreen;

__ds_ns.HomeScreen = __ds_scope.HomeScreen;

__ds_ns.ProjectScreen = __ds_scope.ProjectScreen;

})();

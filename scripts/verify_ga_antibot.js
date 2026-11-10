const fs = require('fs');
const vm = require('vm');

// 1. Read pages/index.html
const content = fs.readFileSync('pages/index.html', 'utf8');

// Find the specific GA script tag
const matches = [...content.matchAll(/<script data-cfasync="false">([\s\S]*?)<\/script>/g)];
const gaScript = matches.find(m => m[1].includes('ga-disable-G-MYFWHFPSYB'));

if (!gaScript) {
  console.error('GA script not found in pages/index.html!');
  process.exit(1);
}

console.log('[Test 1] Found GA anti-bot script tag in index.html.');

const code = gaScript[1];

// Test case 1: Normal user (should execute gtag config, NOT set ga-disable)
{
  const dataLayer = [];
  const sandbox = {
    window: { screen: { width: 1920, height: 1080 } },
    dataLayer: dataLayer,
    navigator: { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36', webdriver: false },
    document: {
      createElement: (tag) => {
        if (tag === 'canvas') {
          return {
            getContext: () => ({
              getExtension: () => ({ UNMASKED_RENDERER_WEBGL: 1 }),
              getParameter: () => 'ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0, D3D11)'
            })
          };
        }
        return {};
      }
    },
    Date: Date,
    console: console
  };
  sandbox.window.window = sandbox.window;
  sandbox.window.dataLayer = dataLayer;
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox);

  if (sandbox.window['ga-disable-G-MYFWHFPSYB']) {
    console.error('FAIL: Normal user was incorrectly flagged as bot!');
    process.exit(1);
  }
  const configCalls = dataLayer.filter(args => args[0] === 'config' && args[1] === 'G-MYFWHFPSYB');
  if (configCalls.length !== 1) {
    console.error('FAIL: Normal user did not trigger gtag config!');
    process.exit(1);
  }
  console.log('  PASS: Normal user executed gtag config (0ms delay), ga-disable is undefined.');
}

// Test case 2: Headless Bot (navigator.webdriver = true)
{
  const dataLayer = [];
  const sandbox = {
    window: { screen: { width: 1920, height: 1080 } },
    dataLayer: dataLayer,
    navigator: { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)', webdriver: true },
    document: {
      createElement: () => ({ getContext: () => null })
    },
    Date: Date,
    console: console
  };
  sandbox.window.window = sandbox.window;
  sandbox.window.dataLayer = dataLayer;
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox);

  if (sandbox.window['ga-disable-G-MYFWHFPSYB'] !== true) {
    console.error('FAIL: webdriver bot was NOT blocked!');
    process.exit(1);
  }
  const configCalls = dataLayer.filter(args => args[0] === 'config' && args[1] === 'G-MYFWHFPSYB');
  if (configCalls.length > 0) {
    console.error('FAIL: webdriver bot still executed gtag config!');
    process.exit(1);
  }
  console.log('  PASS: navigator.webdriver bot blocked successfully (ga-disable = true, config not called).');
}

// Test case 3: Headless Chrome UA
{
  const dataLayer = [];
  const sandbox = {
    window: { screen: { width: 1920, height: 1080 } },
    dataLayer: dataLayer,
    navigator: { userAgent: 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/120.0.0.0 Safari/537.36', webdriver: false },
    document: {
      createElement: () => ({ getContext: () => null })
    },
    Date: Date,
    console: console
  };
  sandbox.window.window = sandbox.window;
  sandbox.window.dataLayer = dataLayer;
  vm.createContext(sandbox);
  vm.runInContext(code, sandbox);

  if (sandbox.window['ga-disable-G-MYFWHFPSYB'] !== true) {
    console.error('FAIL: HeadlessChrome UA bot was NOT blocked!');
    process.exit(1);
  }
  console.log('  PASS: HeadlessChrome UA bot blocked successfully.');
}

// Test case 4: Datacenter container resolution (e.g. 1280x1200, 1366x1366, square screen)
{
  const testRes = [
    { w: 1280, h: 1200 },
    { w: 1366, h: 1366 },
    { w: 1280, h: 1200 },
    { w: 1280, h: 1280 },
    { w: 1600, h: 1600 },
    { w: 1280, h: 1600 },
    { w: 1600, h: 1200 },
    { w: 800, h: 600 },
    { w: 1000, h: 1000 } // sw > 0 && sw === sh
  ];

  for (const r of testRes) {
    const dataLayer = [];
    const sandbox = {
      window: { screen: { width: r.w, height: r.h } },
      dataLayer: dataLayer,
      navigator: { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36', webdriver: false },
      document: { createElement: () => ({ getContext: () => null }) },
      Date: Date,
      console: console
    };
    sandbox.window.window = sandbox.window;
    sandbox.window.dataLayer = dataLayer;
    vm.createContext(sandbox);
    vm.runInContext(code, sandbox);

    if (sandbox.window['ga-disable-G-MYFWHFPSYB'] !== true) {
      console.error(`FAIL: Datacenter resolution ${r.w}x${r.h} was NOT blocked!`);
      process.exit(1);
    }
  }
  console.log('  PASS: All 8 datacenter/square container resolutions blocked successfully.');
}

// Test case 5: CPU Software Rasterizer (SwiftShader / llvmpipe)
{
  const renderers = [
    'Google SwiftShader',
    'llvmpipe (LLVM 12.0.0, 256 bits)',
    'Software Rasterizer'
  ];

  for (const rend of renderers) {
    const dataLayer = [];
    const sandbox = {
      window: { screen: { width: 1920, height: 1080 } },
      dataLayer: dataLayer,
      navigator: { userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36', webdriver: false },
      document: {
        createElement: (tag) => {
          if (tag === 'canvas') {
            return {
              getContext: () => ({
                getExtension: () => ({ UNMASKED_RENDERER_WEBGL: 1 }),
                getParameter: () => rend
              })
            };
          }
          return {};
        }
      },
      Date: Date,
      console: console
    };
    sandbox.window.window = sandbox.window;
    sandbox.window.dataLayer = dataLayer;
    vm.createContext(sandbox);
    vm.runInContext(code, sandbox);

    if (sandbox.window['ga-disable-G-MYFWHFPSYB'] !== true) {
      console.error(`FAIL: Software renderer "${rend}" was NOT blocked!`);
      process.exit(1);
    }
  }
  console.log('  PASS: CPU software rasterizers (SwiftShader/llvmpipe) blocked successfully.');
}

console.log('\nALL 5 TEST SUITES PASSED FLAWLESSLY!');

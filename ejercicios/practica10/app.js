const puppeteer= require('puppeteer');

const delay = (ms) => new Promise (resolve=>setTimeout(resolve,ms));
(async ()=>{
    const browser =await puppeteer.launch({headless:false});
    const page = await browser.newPage();
    await page.goto('https://www.facebook.com');
    //id=email
    //id=pass
    //'button[name="login"]'
    await page.type ('#email','ares04835@gmail.com')
    {
        await page.type ('#pass','') //en el codigo que suba a github quitare la contraseña
    } // en esta linea oculta esta la contraseña
    await page.$eval('button[name="login"]', el=>el.click())
    await page.screenshot({path:'example.png'});
    console.log('listo manin');
    await delay(10000);
    console.log('gracias por la espera manin');
    await page.screenshot({path:'segundacap.png'});
    console.log('todo listo manito')
    await browser.close();
})()
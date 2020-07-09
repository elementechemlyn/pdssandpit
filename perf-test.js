import http from 'k6/http';
import { check } from 'k6';

// export let options = {
//     stages: [
//         { duration: "1m", target: 5 } // traffic from 1 to 5 users over 1 minutes.
//     ]
// }

export default () => {

    // const jar = http.cookieJar();

    // function getAuthorizeUrl() {
    //     let url = "https://nhsd-apim-testing-internal-dev.herokuapp.com";
    //     let response = http.get(url)
    //     check(response, {
    //         "getAuthorizeUrl status is 200": (r) => r.status === 200
    //     })
    //     let responseBody = JSON.stringify(response.body)
    //     var aTag = responseBody.substring(
    //         responseBody.lastIndexOf("<a"),
    //         responseBody.lastIndexOf("</a>")
    //     )
    //     var authoriseUrl = aTag.replace('<a href=\\"', "")
    //     authoriseUrl = authoriseUrl.replace('\\" id=\\"start\\">Click to Sign In', "")
    //     authoriseUrl = authoriseUrl.split(";").join("&")
    //     return authoriseUrl
    // }

    // function getState(authoriseUrl) {
    //     let response = http.get(authoriseUrl)
    //     check(response, {
    //         "getState status is 200": (r) => r.status === 200
    //     })
    //     var responseUrl = decodeURIComponent(response.url);
    //     let a = (responseUrl.split('='));
    //     let state = a[a.length-1].split('#')[0]
    //     return state;
    // }

    // function getAuthId(state) {
    //     let url = "https://am.nhsspit-2.ptl.nhsd-esa.net/openam/json/realms/root/realms/oidc/authenticate?goto=https%3A%2F%2Fam.nhsspit-2.ptl.nhsd-esa.net%3A443%2Fopenam%2Foauth2%2Frealms%2Froot%2Frealms%2Foidc%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3D969567331415.apps.national%26redirect_uri%3Dhttps%253A%252F%252Finternal-dev.api.service.nhs.uk%252Foauth2%252Fv1%252Fcallback%26scope%3Dopenid%26state%3D" + state;
    //     let params = {
    //         headers: {
    //             'Content-Type': 'application/json',
    //             "Accept-API-Version": "protocol=1.0,resource=2.1"
    //         },
    //     };
    //     let response = http.post(url, "", params);
    //     check(response, {
    //         'getAuthId status is 200': (r) => r.status === 200
    //     })
    //     return JSON.parse(response.body).authId;
    // }

    // function authenticate(authId) {
    //     let url = "https://am.nhsspit-2.ptl.nhsd-esa.net/openam/json/realms/root/realms/oidc/authenticate?goto=https%3A%2F%2Fam.nhsspit-2.ptl.nhsd-esa.net%3A443%2Fopenam%2Foauth2%2Frealms%2Froot%2Frealms%2Foidc%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3D969567331415.apps.national%26redirect_uri%3Dhttps%253A%252F%252Finternal-dev.api.service.nhs.uk%252Foauth2%252Fv1%252Fcallback%26scope%3Dopenid%26state%3D" + state;
    //     let payload = JSON.stringify(
    //         {"authId": authId,"template":"","stage":"DataStore1","header":"Sign in","callbacks":[{"type":"NameCallback","output":[{"name":"prompt","value":"User Name:"}],"input":[{"name":"IDToken1","value":"910000000001"}]},{"type":"PasswordCallback","output":[{"name":"prompt","value":"Password:"}],"input":[{"name":"IDToken2","value":"Password1"}]}]}
    //     )
    //     let params = {
    //         headers: {
    //             'Content-Type': 'application/json',
    //             "Accept-API-Version": "protocol=1.0,resource=2.1"
    //         }
    //     }
    //     let response = http.post(url, payload, params)
    //     check(response, {
    //         'authenticate status is 200': (r) => r.status === 200
    //     })
    //     let responseBody = JSON.parse(response.body)
    //     jar.set(response.cookies)
    //     return {
    //         tokenId: responseBody.tokenId,
    //         successUrl: responseBody.successUrl
    //     }
    // }

    // function tokenExchange(tokenId, successUrl) {
    //     let response = http.get(successUrl)
    //     console.log(JSON.stringify(response.request.url))
    //     check(response, {
    //         'tokenExchange status is 200': (r) => r.status === 200
    //     })
    //     console.log(JSON.stringify(response.body))
    // }

    // let authoriseUrl = getAuthorizeUrl()
    // let state = getState(authoriseUrl)
    // let authId = getAuthId(state);
    // let authenticated = authenticate(authId);
    // tokenExchange(authenticated.tokenId, authenticated.successUrl)

    // let url = "https://internal-dev.api.service.nhs.uk/personal-demographics/Patient?family=Smith&gender=male&birthdate=2010-01-01";
    // let params = {
    //     headers: {
    //         'NHSD-Session-URID': 1234567890,
    //         Authorization: 'Bearer invalid'
    //     }
    // }
    // let apiCall = http.get(url, params)

    // Verify Response
    // check(apiCall, {
    //     'status is 200': (r) => r.status === 200
    // })
}
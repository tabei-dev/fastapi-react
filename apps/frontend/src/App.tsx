import { JSX } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import CssBaseline from '@mui/material/CssBaseline';
import { ThemeProvider } from '@mui/material/styles';
import { RecoilRoot, RecoilEnv } from 'recoil';

import { SideMenuProvider } from '@/common/contexts/sideMenuContext';
import Theme from '@/common/styles/theme';
import SideMenu from '@/domain/modules/SideMenu';
import Login from '@/domain/pages/Login';
import Menu from '@/domain/pages/Menu';
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
// import '@/App.css';
// import axios from '@/config/axios';

RecoilEnv.RECOIL_DUPLICATE_ATOM_KEY_CHECKING_ENABLED = false;

/**
 *
 * @returns {JSX.Element} JSX.Element
 */
const App = (): JSX.Element => {
  // const [count, setCount] = useState(0);
  // const [data, setData] = useState('');

  // useEffect(() => {
  //   (async () => {
  //     try {
  //       const response = await axios.get('/api/data');
  //       setData(response.data.data);
  //     } catch (error) {
  //       console.error('Error fetching data:', error);
  //     }
  //   })();
  // }, []);
  const sideMenu = new SideMenu();

  return (
    <ThemeProvider theme={Theme}>
      <SideMenuProvider value={sideMenu}>
        <CssBaseline />
        <RecoilRoot>
          <Router>
            <Routes>
              <Route index element={<Login />} />
              <Route path="menu" element={<Menu />} />
            </Routes>
          </Router>
        </RecoilRoot>
      </SideMenuProvider>
    </ThemeProvider>
  );
};
export default App;

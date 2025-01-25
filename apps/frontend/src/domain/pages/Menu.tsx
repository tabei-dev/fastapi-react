import { useEffect } from 'react';

import { useSetRecoilState } from 'recoil';

import Page from '@/common/components/Page';
import { selectedCategoryAndPageState } from '@/common/recoil/recoil';
import { PAGES } from '@/domain/config/consts';

const Menu = () => {
  const setSelectedCategoryAndPage = useSetRecoilState(selectedCategoryAndPageState);

  useEffect(() => {
    setSelectedCategoryAndPage({
      category: '',
      page: PAGES.MENU,
    });
  }, [setSelectedCategoryAndPage]);

  return (
    <Page page={PAGES.MENU}>
      <h1>Menu</h1>
    </Page>
  );
};
export default Menu;

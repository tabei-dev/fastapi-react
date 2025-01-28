import { JSX } from 'react';

import { PAGES } from '@/domain/config/consts';
import Page from '@/shared/components/Page';
// import useCategoryAndPage from '@/shared/hooks/useCategoryAndPage';
import { useSetSelectedPage } from '@/shared/contexts/pageContext';

/**
 * メニューページ
 * @returns {JSX.Element} JSX.Element
 */
const Menu = (): JSX.Element => {
  // useCategoryAndPage({ category: '', page: PAGES.MENU });
  useSetSelectedPage({ categoryName: '', pageName: PAGES.MENU });

  return (
    <Page>
      <h1>Menu</h1>
    </Page>
  );
};
export default Menu;

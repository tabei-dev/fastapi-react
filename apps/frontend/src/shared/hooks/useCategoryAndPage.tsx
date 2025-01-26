import { useEffect } from 'react';

// import { useSetRecoilState } from 'recoil';
import { useSetAtom } from 'jotai';

import { selectedCategoryAndPageState } from '@/shared/jotai/jotai';

const useCategoryAndPage = ({ category, page }: { category: string; page: string }) => {
  const setSelectedCategoryAndPage = useSetAtom(selectedCategoryAndPageState);

  useEffect(() => {
    setSelectedCategoryAndPage({
      category,
      page,
    });
  }, [category, page, setSelectedCategoryAndPage]);
};
export default useCategoryAndPage;

import React from 'react';
import { render } from '@testing-library/react';
import Header from '../../src/components/Header';

test('renders header', () => {
  const { getByText } = render(<Header />);
  const headerElement = getByText(/Pflege-App/i);
  expect(headerElement).toBeInTheDocument();
});
